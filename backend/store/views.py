from django.shortcuts import render
from . import models,serializers
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from django.db.models import Q
# Create your views here.

@api_view(['POST'])
def search(request):
    query = request.data.get('query','')
    if query:
        products = Product.objects.filter(Q(title__icontains=query)|Q(description__icontains=query))
        serializer = serializers.ProductSerializerList(products,many=True)
        return Response(serializer.data,status=200)
    else:
        return Response(data={"products":[]})



@api_view(['GET'])
def navCategories(request):
    data = models.Category.objects.all()
    serializer = serializers.NavCategorySerializer(data,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def latestProducts(request):
    data = models.Product.objects.all().order_by('-created')[:20]
    serializer = serializers.ProductSerializerList(data,many=True)
    return Response(serializer.data)

class CategoryViewSet(NestedViewSetMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,GenericViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    lookup_field='slug'


class SubCategoryViewSet(NestedViewSetMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,GenericViewSet):
    queryset = models.SubCategory.objects.all()
    serializer_class = serializers.SubCategorySerializer
    lookup_field='slug'


class ProductViewSet(NestedViewSetMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,GenericViewSet):
    queryset = models.Product.objects.all()
    lookup_field='slug'
    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ProductSerializerList
        if self.action == 'retrieve':
            return serializers.ProductSerializerDetail

