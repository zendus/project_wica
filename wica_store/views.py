from django.shortcuts import render
from .models import *

products = Product.objects.all()
context = {
        'products': products
    }

def store(request):
    return render(request, 'wica_store/store.html', context)

def books(request):
    return render(request, 'wica_store/books.html', context)

def men_fashion(request):
    return render(request, 'wica_store/men_fashion.html', context)

def women_fasion(request):
    return render(request, 'wica_store/women_fashion.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, order_complete=False)
        items = order.orderitem_set.all()
    else:
        items = {}
        order = {
            'get_cart_items_total_quantity': 0,
            'get_cart_items_total_price': 0
        }
    context = {
        'items': items,
        'order': order
    }
    return render(request, 'wica_store/cart.html', context)

def checkout(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, order_complete=False)
        items = order.orderitem_set.all()
    else:
        items = {}
        order = {
            'get_cart_items_total_quantity': 0,
            'get_cart_items_total_price': 0
        }
    context = {
        'items': items,
        'order': order
    }
    return render(request, 'wica_store/checkout.html', context)