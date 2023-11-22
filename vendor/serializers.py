from rest_framework import serializers
from testify.models import Vendor, VendorReview, VendorFollower, Product
from account.models import Account
from testify.serializers import ProductColorSerializer


class VendorSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Vendor
        fields = "__all__"


class VendorReview(serializers.ModelSerializer):
    class Meta:
        model = VendorReview
        fields = "__all__"


class VendorFollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorFollower
        fields = "__all__"


class ProductWithColorSerializer(serializers.ModelSerializer):
    colors = ProductColorSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
