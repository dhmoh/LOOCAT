# project urls.py
from django.contrib import admin
from django.urls import path, include
from .views import register, login_v, logout_v

urlpatterns = [
    path('register/', register, name='register'),
    path('', login_v, name='login_v'),
    path('logout/', logout_v, name='logout_v')
]



