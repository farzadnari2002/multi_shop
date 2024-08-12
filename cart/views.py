from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from products.models import Product


class CartDetail(View):
    def get(self, request):
        return render(request, 'cart/cart_detail.html')
    

class CartAdd(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk)
        size, color, quantity = request.POST.get('size'), request.POST.get('color'), request.POST.get('quantity')
        print('product added')
        return redirect('cart:cart_detail')