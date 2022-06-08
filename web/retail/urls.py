# project urls.py
from django.contrib import admin
from django.urls import path, include
from .views import product_v

urlpatterns = [
    path('home/', product_v, name='product_v'),
]
