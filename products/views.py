from typing import Any
from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, ListView
from .models import *


class ProductDetail(DetailView):
    model = Product


class NevbarPartialView(TemplateView):
    template_name = 'includes/nevbar.html'

    def get_context_data(self, **kwargs):
        context = super(NevbarPartialView, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context
    

class ProductsList(ListView):
    template_name = 'products/products_list.html'
    queryset = Product.objects.all()
    
    def get_context_data(self, **kwargs):
        request = self.request
        colors = request.GET.getlist('color')
        sizes = request.GET.getlist('size')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        queryset = Product.objects.all()
        for product in queryset:
            print(product.price)
        if sizes:
            queryset = queryset.filter(color__title__in=colors).distinct()
        if colors:
            queryset = queryset.filter(color__title__in=colors).distinct()
        if min_price and max_price:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)       
        context = super(ProductsList, self).get_context_data()
        context['object_list'] = queryset
        return context
    



