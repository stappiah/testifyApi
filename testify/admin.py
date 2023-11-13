from django.contrib import admin
from .models import Product, Order, OrderItem, Color

# Register your models here.
admin.site.register(Product)
admin.site.register(Color)