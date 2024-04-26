from django import forms


class LoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={
         "type":"tel",
         "class":"form-control",
         "id":"phone",
         "placeholder":"Your Phone",
         "required":"required",
         "data-validation-required-message":"Please enter your phone number", }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
         "type":"password",
         "class":"form-control",
         "id":"password",
         "placeholder":"Your Password",
         "required":"required",
         "data-validation-required-message":"Please enter your password",
    }))
