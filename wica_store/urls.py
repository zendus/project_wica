from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('books/', views.books, name='books'),
    path('fashion/men/', views.men_fashion, name='men_fashion'),
    path('fashion/women/', views.women_fasion, name='women_fashion'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]