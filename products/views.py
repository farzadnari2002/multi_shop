from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product


class ProductDetail(DetailView):
    model = Product
