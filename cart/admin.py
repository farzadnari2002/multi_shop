from django.contrib import admin
from .models import *


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_paid')
    inlines = (OrderItemAdmin,)
    list_filter = ('is_paid',)


@admin.register(DiscountCode)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount', 'quantity')

