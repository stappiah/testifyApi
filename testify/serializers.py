from .models import (
    Product,
    Order,
    OrderItem,
    Vendor,
    ProductReview,
    VendorReview,
    Wishlist,
    Color,
    ProductSize,
    ProductImage,
)
from rest_framework import serializers
from account.models import Account
from decimal import Decimal
from django.db.models import Sum


class ProductColorSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Color
        fields = "__all__"


class ProductSizeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = ProductSize
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )

    colors = ProductColorSerializer(many=True, read_only=True)
    sizes = ProductSizeSerializer(many=True, read_only=True)
    vendor_name = serializers.SerializerMethodField()
    vendor_address = serializers.SerializerMethodField()
    vendor_region = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_vendor_name(self, obj):
        if obj.vendor:
            return obj.vendor.shop_name
        return "No Vendor"

    def get_vendor_address(self, obj):
        if obj.vendor:
            return obj.vendor.address
        return "No Vendor"

    def get_vendor_region(self, obj):
        if obj.vendor:
            return obj.vendor.region
        return "No Vendor"

    def get_rating(self, obj):
        ratings = obj.rating.all()
        if ratings.exists():
            total_ratings = ratings.aggregate(total=Sum("rating"))["total"]
            num_ratings = ratings.count()
            return round(Decimal(total_ratings / num_ratings), 1)
        return None


class ProductImageSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = ProductImage
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = OrderItem
        fields = "__all__"


class ProductReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )

    user_first_name = serializers.SerializerMethodField()
    user_last_name = serializers.SerializerMethodField()

    class Meta:
        model = ProductReview
        fields = "__all__"

    def get_user_first_name(self, obj):
        if obj.user:
            return obj.user.first_name
        else:
            return "No first name"

    def get_user_last_name(self, obj):
        if obj.user:
            return obj.user.last_name
        else:
            return "No last name"


class WishListSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Wishlist
        fields = "__all__"


class GetWishListSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )

    product = ProductSerializer()

    class Meta:
        model = Wishlist
        fields = "__all__"
