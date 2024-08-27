from django.urls import path
from .views import *


app_name = 'accounts'

urlpatterns = [
    path('login', Login.as_view(), name="login"),
    path('registerloginotp', RegisterLoginOtp.as_view(), name="register_login_otp"), 
    path('checkotp', CheckOtp.as_view(), name="check_otp"),
    path('logout', Logout.as_view(), name="logout"),
    path('add/address', AddAddress.as_view(), name='add_address'),
]
