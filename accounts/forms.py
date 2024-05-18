from django import forms
from django.core.validators import MaxLengthValidator
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
         "type":"",
         "class":"form-control",
         "id":"username",
         "placeholder":"phone or email",
         "required":"required",
         "data-validation-required-message":"Please enter your phone or email",
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
         "type":"password",
         "class":"form-control",
         "id":"password",
         "placeholder":"Your Password",
         "required":"required",
         "data-validation-required-message":"Please enter your password",
    }))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) > 100:
            raise ValidationError('تلفن یا ایمیل وارد شده معتبر نیست', code='invalid_username')
        return username 
        

class RegisterForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={
         "type":"tel",
         "class":"form-control",
         "id":"phone",
         "placeholder":"Your Phone",
         "required":"required",
         "data-validation-required-message":"Please enter your phone number", }))
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) != 11:
            raise ValidationError('تلفن وارد شده معتبر نیست', code='invalid_phone')
        return phone
        
class CheckOtpForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
         "type":"tel",
         "class":"form-control",
         "id":"phone",
         "placeholder":"Code",
         "required":"required",
         "data-validation-required-message":"Please enter verify code", }))
    
    def clean_phone(self):
        phone = self.cleaned_data.get('code')
        if len(phone) != 11:
            raise ValidationError('کد وارد شده معتبر نیست', code='invalid_code')
        return phone
        
    


