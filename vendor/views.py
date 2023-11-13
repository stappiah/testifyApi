from rest_framework import generics
from rest_framework import permissions, authentication, serializers
from testify import models
from vendor import serializers

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
