from django.forms import ModelForm

from .models import *

class ProductForm(ModelForm):
    class Meta:
        model = product
        fields = ['name', 'k_name', 'price', 'quant', 'info']