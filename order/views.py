from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.mixins import RetrieveModelMixin,UpdateModelMixin,CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from .serializers import UserSerializer
from rest_framework import permissions,status,authentication
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes,permission_classes
import stripe
from django.conf import settings
from django.http import Http404
from django.shortcuts import render

from .models import Order,OrderItem
from .serializers import StripeOrderSerializer,PaymobOrderSerializer, OrderItemSerializer

import requests


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def paymob_payment(request):
    serializer = PaymobOrderSerializer(data=request.data)

    if serializer.is_valid():
        api_key = settings.PAYMOB_SECRET_KEY
        first_response = requests.post(url='https://accept.paymob.com/api/auth/tokens',
                                       headers={'Content-Type':'application/json'},
                                       json={"api_key":api_key})
        first_json = first_response.json()
        auth_token = first_json["token"]
        items = []
        for item in serializer.validated_data["items"]:
            items.append({
                "name":item.get('product').title,
                "amount_cents":int(item.get('quantity')*item.get('product').price * 100),
                "quantity":item.get('quantity')
            })
        paid_amount = sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data['items'])*100
        print(paid_amount)
        second_data = {
            "auth_token":auth_token,
            "delivery_needed":"false",
            "amount_cents": int(paid_amount),
            "currency": "EGP",
            "items":items
        }
        second_response = requests.post(url='https://accept.paymob.com/api/ecommerce/orders',
                                        headers={'Content-Type':'application/json'},
                                        json=second_data)
        second_json = second_response.json()
        order_id = second_json["id"]
        third_data = {
            "auth_token": auth_token,
            "amount_cents": "100", 
            "expiration": 3600, 
            "order_id": order_id,
            "billing_data": {
                "apartment": "NA",
                "floor": "NA", 
                "street": "NA", 
                "building": "NA", 
                "city": "NA", 
                "country": "NA",
                "email": serializer.validated_data["email"], 
                "first_name": serializer.validated_data["first_name"], 
                "phone_number": serializer.validated_data["phone"], 
                "last_name": serializer.validated_data["last_name"], 
            }, 
            "currency": "EGP", 
            "integration_id": 3317273
        }
        third_response = requests.post(url='https://accept.paymob.com/api/acceptance/payment_keys',
                                        headers={'Content-Type':'application/json'},
                                        json=third_data)
        third_json = third_response.json()
        token =  third_json["token"]
        serializer.save(user = request.user)
        return Response(data={"token":token},status=200)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = StripeOrderSerializer(data=request.data)

    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amount = sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data['items'])

        try:
            charge = stripe.Charge.create(
                amount=int(paid_amount * 100),
                currency='USD',
                description='Charge from E Store',
                source=serializer.validated_data['stripe_token']
            )

            serializer.save(user=request.user, paid_amount=paid_amount)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def reset_password(request):
    data = request.data
    user = User.objects.get(pk= request.user.id)
    if (user.check_password(data['currentPassword'])):
        user.set_password(data["newPassword"])
        user.save()
        return Response({"message":"Password Changed successfully"},status=200)
    else:
        return Response({"message":"Invalid current password. Please enter your current password."},status=400)




class UserViewset(APIView):
    def get_permissions(self):
        if self.request.method == 'GET' or self.request.method == 'PATCH':
            return [permissions.IsAuthenticated(),]
        return super().get_permissions()



    def get(self,request):
        user = User.objects.get(pk=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    def patch(self,request):
        user = User.objects.get(pk=request.user.id)
        data = request.data
        serializer = UserSerializer(instance=user,data=data)
        if (request.user.email != data['email'] or request.user.username != data["username"]):
            try:
                User.objects.get(email = data["email"])
                return Response({"message":"A user with that email already exists."},status=400)
            except User.DoesNotExist:
                if (request.user.username != data["username"]):
                    try:
                        User.objects.get(username = data["username"])
                        return Response({"message":"A user with that username already exists"},status=400)
                    except User.DoesNotExist:
                        if serializer.is_valid():
                            serializer.save()
                            return Response(serializer.data)
                        else:
                            return Response(serializer.errors,status=400)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=400)
    def post(self,request):
        data = request.data
        try:
            User.objects.get(username = data["username"])
            return Response({"message":"This username is not Available. Please change your username."},status=400)
        except User.DoesNotExist:
            try:
                User.objects.get(email = data["email"])
                return Response({"message":"This email address  is not available. Please change your email address."})
            except User.DoesNotExist:
                user = User(username=data["username"])
                user.set_password(data["password"])
                user.first_name = data["first_name"]
                user.last_name = data["last_name"]
                user.email = data["email"]
                user.save()
                return Response({"message":"Sign up successful.Signing in and redirecting to home page."})