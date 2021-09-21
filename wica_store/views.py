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
    return render(request, 'wica_store/cart.html')

def checkout(request):
    return render(request, 'wica_store/checkout.html')