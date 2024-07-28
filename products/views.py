from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'products'