from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import LoginForm, RegisterForm, CheckOtpForm
from django.contrib.auth import authenticate, login
import ghasedakpack
from random import randint
from .models import User, Otp
from uuid import uuid4


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
    

class RegisterLoginOtp(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'accounts/register_login_otp.html', context={'form':form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            randcode = randint(10000,99999)
            SMS.verification({'receptor': cd['phone'], 'type': 'type1', 'template': 'randcode', 'param1': randcode})
            token = str(uuid4())
            Otp.objects.create(token=token, phone=cd['phone'], code=randcode)
            print(randcode)
            return redirect(reverse('accounts:check_otp') + f'?token={token}')
        else:
            form.add_error('phone', 'invalid user data')

        return render(request, 'accounts/register.html', context={'form':form})


class CheckOtp(View):
    def get(self, request):
        form = CheckOtpForm()
        return render(request, 'accounts/check_otp.html', context={'form':form})
    
    def post(self, request):
        form = CheckOtpForm(request.POST)
        token = request.GET.get('token')
        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(token=token, code=cd['code']).exists():
                otp = Otp.objects.get(token=token)
                user, is_created  = User.objects.get_or_create(phone=otp.phone)
                login(request, user)
                otp.delete()
                return redirect('/')
        else:
            form.add_error('phone', 'invalid user data')

        return render(request, 'accounts/check_otp.html', context={'form':form})
    
    
            
    