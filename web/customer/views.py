from django.shortcuts import render, redirect
from datetime import datetime
from .models import *
from accounts.models import *
from retail.models import *

def customer_home(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('')
    if request.method == "POST":
        user_id = user.id
        enter = Enter(
            user=user_id,
        )
        enter.save()
        return render(request, 'shopping.html')
    else:
        return render(request, 'home.html')

def shopping(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('')
    return render(request, 'shopping.html')

def payment_v(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('')
    else:
        pay = PAYMENT.objects.select_related('product_id').filter(user=user.id)
        pay_sum = 0
        datetime_format = "%Y-%m-%d %H:%M:%S"
        for p in pay:
            p.product_id.price *= p.quant
            pay_sum += p.product_id.price
            print(p.date_time)
            str_time = str(p.date_time).split('+')[0]
            p.date_time = datetime.strptime(str_time, datetime_format)
            print(p.date_time)

        context = {
            'pay': pay,
            'pay_sum':pay_sum,
        }
        return render(request, 'payment.html', context)

