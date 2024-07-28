from django.urls import path
from .views import *

app_name = 'products'
urlpatterns = [
    path('<int:pk>', ProductDetail.as_view(), name='product_detail')
]


