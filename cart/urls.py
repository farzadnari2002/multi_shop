from django.urls import path
from .views import *


app_name = 'cart'
urlpatterns = [
    path('detail',CartDetail.as_view(), name='cart_detail')
]
