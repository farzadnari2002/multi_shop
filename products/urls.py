from django.urls import path
from .views import *


app_name = 'products'
urlpatterns = [
    path('', ProductsList.as_view(), name='products_list'),
    path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('nevbarpartial', NevbarPartialView.as_view(), name='nevbar'),
] 


