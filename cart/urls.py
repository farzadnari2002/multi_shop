from django.urls import path
from .views import *


app_name = 'cart'
urlpatterns = [
    path('detail',CartDetail.as_view(), name='cart_detail'),
    path('add/<int:pk>',CartAdd.as_view(), name='cart_add'),
    path('delete/<str:id>',CartDelete.as_view(), name='cart_delete'),
    path('order/create', OrderCreate.as_view(), name='order_create'),
]
