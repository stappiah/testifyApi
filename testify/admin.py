from django.contrib import admin
from .models import Product, Order, OrderItem, Color, Wishlist, Vendor

# Register your models here.
admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Wishlist)
admin.site.register(Vendor)