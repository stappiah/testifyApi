from rest_framework import generics, parsers
from rest_framework import permissions, authentication, serializers
from testify import models
from vendor import serializers
from account.models import Account
from rest_framework.response import Response
from testify.serializers import ProductSerializer
from django.db.models import Q, Avg
from decimal import Decimal

# Create your views here.


class VendorCreationView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.VendorSerializer
    parser_classes = [parsers.MultiPartParser]
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


class GetVendorProducts(generics.ListAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        vendor_id = self.kwargs.get("pk")
        vendor = models.Vendor.objects.get(id=vendor_id)
        queryset = models.Product.objects.filter(vendor=vendor)
        return queryset


class GetVendors(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.VendorSerializer
    queryset = models.Vendor.objects.all()


class SearchVendorProduct(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = ProductSerializer

    def get_queryset(self):
        # Get the vendor based on the provided primary key (pk) in the URL
        vendor_id = self.kwargs.get("pk")
        try:
            vendor = models.Vendor.objects.get(id=vendor_id)
        except models.Vendor.DoesNotExist:
            return (
                models.Product.objects.none()
            )  # Return an empty queryset if the vendor is not found

        # Get the products related to the vendor
        queryset = models.Product.objects.filter(vendor=vendor)

        # Search query parameter
        search_query = self.request.query_params.get("q", None)

        # Apply search filter if a search query is provided
        if search_query:
            # Using Q objects to create complex queries
            queryset = queryset.filter(
                Q(name__icontains=search_query)
                | Q(product_brand__icontains=search_query)
                | Q(product_category__icontains=search_query)
                | Q(vendor__shop_name__icontains=search_query)
            )

        return queryset


class VendorAverageRating(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.VendorReviewSerializer

    def get(self, request, pk):
        vendor_id = models.Vendor.objects.get(id=pk)
        rating = models.VendorReview.objects.filter(vendor=vendor_id)
        if len(rating) != 0:
            average_rating = rating.aggregate(avg_rating=Avg("rating"))["avg_rating"]
            average_rating = round(Decimal(average_rating), 1)
            return Response({"average_rating": average_rating})
        return Response({"response": "No rating"})


class VendorReviewCreation(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.VendorReviewSerializer
    queryset = models.VendorReview.objects.all()


class GetVendorReview(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.VendorReviewSerializer

    def get_queryset(self):
        vendor_id = self.kwargs.get("pk")
        vendor = models.Vendor.objects.get(id=vendor_id)
        review = models.VendorReview.objects.filter(vendor=vendor)
        return review
