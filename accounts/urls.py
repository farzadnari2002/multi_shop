from django.urls import path
from .views import Login, Register


app_name = 'accounts'

urlpatterns = [
    path('login', Login.as_view(), name="login"),
    path('register', Register.as_view(), name="register"), 
]
