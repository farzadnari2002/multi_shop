from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from products.models import Product
from .cart_module import Cart


class CartDetail(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'cart/cart_detail.html', context={'cart':cart})
    

class CartAdd(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        size, color, quantity = request.POST.get('size', 'empty'), request.POST.get('color', 'empty'), request.POST.get('quantity', 'empty')
        cart = Cart(request)
        cart.add(product, color, size, quantity)
        return redirect('cart:cart_detail')
    

class CartDelete(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.delete(id)
        return redirect('cart:cart_detail')