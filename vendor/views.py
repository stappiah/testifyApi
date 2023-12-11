from rest_framework import generics
from rest_framework import permissions, authentication, serializers
from testify import models
from vendor import serializers
from account.models import Account
from rest_framework.response import Response
from testify.serializers import ProductSerializer
from django.db.models import Q

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


class FollowVendor(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.VendorFollowerSerializer
    queryset = models.VendorFollower.objects.all()


class CheckVendorFollower(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.VendorFollowerSerializer

    def get(self, request, pk):
        try:
            vendor = models.Vendor.objects.get(id=pk)
            follower = models.VendorFollower.objects.get(
                follower=request.user, vendor=vendor
            )
            return Response({"response": "User is following vendor"})
        except models.VendorFollower.DoesNotExist:
            return Response({"response": "User is not following vendor"}, status=404)


class UnFollowVendor(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.VendorFollowerSerializer

    def delete(self, request, pk):
        try:
            vendor = models.Vendor.objects.get(id=pk)
            follower = models.VendorFollower.objects.get(
                follower=request.user, vendor=vendor
            )
            follower.delete()
            return Response({"response": "Follower removed successfully"})
        except models.VendorFollower.DoesNotExist:
            return Response({"response": "Follower does not exist"}, status=404)


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

    def get(self, request, pk):
        vendor = models.Vendor.objects.get(id=pk)
        product = models.Product.objects.filter(vendor=vendor)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


class GetVendors(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.VendorSerializer
    queryset = models.Vendor.objects.all()


class SearchVendorProduct(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    # serializer_class = ProductSerializer

    def get(self, request, pk):
        vendor = models.Vendor.objects.get(id=pk)
        product = models.Product.objects.filter(vendor=vendor)
        serializer = ProductSerializer(product, many=True)
        return serializer.data

        # q = self.request.query_params.get("q")
        # if q:
        #     # product = product.filter(name__icontains=q)
        #     product = product.filter(
        #         Q(name__icontains=q)
        #         | Q(product_brand__icontains=q)
        #         | Q(product_category__icontains=q)
        #         | Q(vendor__shop_name__icontains=q)
        #     )
        #     return product
            
