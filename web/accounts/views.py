from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def register(request):
    user = request.user
    if user.is_authenticated:
        if user.is_admin:
            return redirect('/retail/home')
        return redirect('/customer/home')

    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            if user.is_admin:
                return redirect('/retail/home')
            return redirect('/customer/home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'register.html', context)

def login_v(request):
    user = request.user
    if user.is_authenticated:
        if user.is_admin:
            return redirect('/retail/home')
        return redirect('/customer/home')
    form = loginForm
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_admin:
                return redirect('/retail/home')
            return redirect('/customer/home')
        else:
            context = {
                'form':form,
                'error':'이메일 또는 비밀번호가 정확하지 않습니다.',
            }
            return render(request, 'login.html',context)
    else:
        context = {
            'form':form
        }
        return render(request, 'login.html', context)

def logout_v(request):
    logout(request)
    return redirect('/')


    






