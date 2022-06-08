from django.contrib import admin
from .models import *


class reatiladmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'k_name', 'price', 'quant', 'info', 'is_active']
    list_filter = ('is_active',)
    search_fields = ('name', 'k_name',)
    ordering = ('name', 'k_name', 'quant')



admin.site.register(product, reatiladmin)
