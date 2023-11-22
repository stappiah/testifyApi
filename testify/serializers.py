from .models import Product, Order, OrderItem, Vendor, ProductReview, VendorReview, Wishlist, Color, ProductSize, ProductImage
from rest_framework import serializers
from account.models import Account
# from vendor.serializers import VendorSerializer

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
    
    # def get_vendor_shop_name(self, obj):
    #     return obj.vendor.shop_name


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

    class Meta:
        model = ProductReview
        fields = "__all__"


class WishListSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Wishlist
        fields = "__all__"
