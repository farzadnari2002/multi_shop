from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
import ghasedakpack
from random import randint


SMS = ghasedakpack.Ghasedak("56c1f7b271564b46a485083e3afbbccfcf64c5931a189c01866244eeddc6b98c")

class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'accounts/login.html', context={'form':form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error('phone', 'invalid user data')

        return render(request, 'accounts/login.html', context={'form':form})
    

class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'accounts/register.html', context={'form':form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            randcode = randint(1000,9999)
            SMS.verification({'receptor': cd['phone'], 'type': 'type1', 'template': 'randcode', 'param1': randcode})
        else:
            form.add_error('phone', 'invalid user data')

        return render(request, 'accounts/register.html', context={'form':form})
    
            
    