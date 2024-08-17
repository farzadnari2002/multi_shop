from django.urls import path
from .views import *
from django.conf.urls.static import static
from multi_shop import settings


app_name = 'products'
urlpatterns = [
    path('<int:pk>', ProductDetail.as_view(), name='product_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


