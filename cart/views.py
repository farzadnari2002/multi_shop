from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from products.models import Product
from .cart_module import Cart
from .models import *


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
    

class OrderCreate(View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user, total_price=cart.totalprice())
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                color=item['color'],
                size=item['size'],
                quantity=item['quantity'],
                price=item['price'],
                total_price=int(item['quantity']) * int(item['price']),
            )
        cart.remove()
        return redirect('cart:order_detail', order.id)
    

class OrderDetail(View):
    def get(self, request, id):
        order = get_object_or_404(Order, id=id)
        return render(request, 'cart/order_detail.html', {'order':order})
    

class ApplyDiscount(View):
    def post(self, request, id):
        discount = request.POST.get('discount_code')
        order = get_object_or_404(Order, id=id)
        discount_code = get_object_or_404(DiscountCode, name=discount)
        print(discount, order.total_price)
        if discount_code.quantity == 0:
            return redirect('cart:order_detail', order.id)
        order.total_price -= order.total_price * discount_code.discount/100
        order.save()
        discount_code.quantity -= 1
        discount_code.save()
        return redirect('cart:order_detail', order.id)
        
