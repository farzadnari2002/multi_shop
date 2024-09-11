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
    



