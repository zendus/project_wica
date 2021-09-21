from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    CHOICES = (
        ('book', 'BOOK'),
        ('men_fashion', 'MEN FASHION'),
        ('women_fashion', 'WOMEN FASHION'),
    )

    name = models.CharField(max_length=250, null=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    digital = models.BooleanField(default=False, null=True, blank=False)
    section = models.CharField(max_length=100, choices=CHOICES, null=True)
    author_or_brand = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try: 
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    order_complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=250, null=True)

    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=250, null=False)
    city = models.CharField(max_length=250, null=False)
    state = models.CharField(max_length=250, null=False)
    zipcode = models.CharField(max_length=250, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
