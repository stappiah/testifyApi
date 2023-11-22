from rest_framework import generics
from rest_framework import permissions, authentication, serializers
from testify import models
from vendor import serializers
from account.models import Account
from rest_framework.response import Response
from testify.serializers import ProductSerializer

# Create your views here.


class VendorCreationView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.VendorSerializer
    queryset = models.Vendor.objects.all()


class RetrieveUpdateVendorView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.VendorSerializer
    queryset = models.Vendor.objects.all()


class GetFollowers(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.VendorFollowerSerializer

    def get_queryset(self, pk):
        vendor = models.Vendor.objects.get(id=pk)
        followers = models.VendorFollower.objects.filter(vendor=vendor)
        return followers


class GetUserShops(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.VendorSerializer

    def get_queryset(self):
        vendor = models.Vendor.objects.filter(user=self.request.user)
        return vendor


class GetVendorProducts(generics.GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request, pk):
        vendor = models.Vendor.objects.get(id=pk)
        product = models.Product.objects.filter(vendor=vendor)
        serializer = serializers.ProductWithColorSerializer(product, many=True)
        return Response(serializer.data)

# class 