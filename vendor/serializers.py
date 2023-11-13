from rest_framework import serializers
from testify.models import Vendor, VendorReview, VendorFollower


class VendorSerializer(serializers.ModelSerializer):
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