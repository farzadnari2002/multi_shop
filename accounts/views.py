from django.shortcuts import render
from django.views import View
from . import forms


class Login(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, 'accounts/login.html', context={'form':form})