from django.urls import path
from . import views

urlpatterns = [
    path('user/',views.UserViewset.as_view()),
    path('account/reset-pass',views.reset_password),
    path('checkout/',views.checkout),
    path('pay/paymob/',views.paymob_payment)
]