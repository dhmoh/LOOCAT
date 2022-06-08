# project urls.py
from django.contrib import admin
from django.urls import path, include
from .views import customer_home, shopping, payment_v
urlpatterns = [
    path('home/', customer_home, name='customer_home'),
    path('shopping/', shopping, name='shopping'),
    path('payment/', payment_v, name='payment_v')
]
