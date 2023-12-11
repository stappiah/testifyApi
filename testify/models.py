from django.db import models
from account.models import Account

# Create your models here.
LOCATION_REGION = [
    ("Upper West Region", "Upper West Region"),
    ("Upper East Region", "Upper East Region"),
    ("North East Region", "North East Region"),
    ("Northern Region", "Northern Region"),
    ("Savannah Region", "Savannah Region"),
    ("Bono East Region", "Bono East Region"),
    ("Brong Ahafo Region", "Brong Ahafo Region"),
    ("Oti Region", "Oti Region"),
    ("Volta Region", "Volta Region"),
    ("Eastern Region", "Eastern Region"),
    ("Ashanti Region", "Ashanti Region"),
    ("Ahafo Region", "Ahafo Region"),
    ("Western North Region", "Western North Region"),
    ("Western Region", "Western Region"),
    ("Central Region", "Central Region"),
    ("Greater Accra Region", "Greater Accra Region"),
]


ORDER_STATUS = [
    ("Pending", "Pending"),
    ("Canceled", "Canceled"),
    ("Completed", "Completed"),
    ("Processing", "Processing"),
    ("Shipped", "Shipped"),
    ("Refunded", "Refunded"),
    ("Delivered", "Delivered"),
    ("On Hold", "On Hold"),
    ("Pending Payment", "Pending Payment"),
    ("Pending Failed", "Pending Failed"),
]

COLORS = [
    ("red", "red"),
    ("blue", "blue"),
    ("black", "black"),
    ("white", "white"),
    ("green", "green"),
]


class Product(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    vendor = models.ForeignKey(
        "Vendor", on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    description = models.TextField(null=True, blank=True)
    stock_quantity = models.PositiveIntegerField(null=True, blank=True)
    product_brand = models.CharField(max_length=100, null=True, blank=True)
    product_category = models.CharField(max_length=100, null=True, blank=True)
    product_image = models.ImageField(upload_to="product_images", null=True, blank=True)
    approved = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to="product_images/")


class Color(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="colors"
    )
    color = models.CharField(choices=COLORS, max_length=5)


class ProductSize(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sizes")
    size = models.CharField(max_length=3)


class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through="OrderItem")
    shipping_address = models.CharField(max_length=250, null=True, blank=True)
    # billing_address = models.ForeignKey('Address', related_name='billing_address', on_delete=models.CASCADE)
    # payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, null=True, blank=True)
    # Use choices for status tracking
    order_status = models.CharField(choices=ORDER_STATUS, max_length=15)
    date_ordered = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.pk}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.product.discount_price:
            self.price = self.product.discount_price * self.quantity
            super().save(*args, **kwargs)
        else:
            self.price = self.product.price * self.quantity
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} - {self.size} - {self.color}"


class Vendor(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    region = models.CharField(choices=LOCATION_REGION, max_length=20)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField(null=True, blank=True)
    vendor_logo = models.ImageField(upload_to="vendor_logos", null=True, blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.shop_name


class VendorFollower(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    follower = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_started = models.DateTimeField(auto_now_add=True)


class ProductReview(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="rating"
    )
    rating = models.FloatField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class VendorReview(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    comment = models.TextField()


class Wishlist(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="wishlists", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}'s Wishlist"
