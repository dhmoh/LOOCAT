from django.shortcuts import render, redirect
from .forms import *
from retail.models import product

# Create your views here.
def product_v(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('')
    if request.method =='POST':
        name = request.POST['name']
        k_name = request.POST['k_name']
        price = request.POST['price']
        quant = request.POST['quant']
        info = request.POST['info']

        p = product(
            name=name,
            k_name=k_name,
            price=price,
            quant=quant,
            info=info,
        )
        p.save()
        return redirect('product_v')
    else:
        productform = ProductForm
        p = product.objects.all()
        context = {
            'productform' : productform,
            'product' : p,
        }
        return render(request, 'product.html', context)
