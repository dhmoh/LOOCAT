from django.contrib import admin
from .models import *
# Register your models here.

class adminEnter(admin.ModelAdmin):
    list_display = ['id', 'user', 'enter_date', 'is_enter', 'detect_id']

class adminPayment(admin.ModelAdmin):
    list_display = ['user', 'product_id', 'quant', 'date_time']
    search_fields = ('user', 'product_id')
    ordering = ('date_time',)


admin.site.register(Enter, adminEnter)
admin.site.register(PAYMENT, adminPayment)


