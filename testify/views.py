from django.shortcuts import render
from . import serializers
from . import models
from rest_framework import permissions, authentication, generics, response, status
from rest_framework.parsers import MultiPartParser
from rest_framework.request import Request
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.db.models import Q
from vendor.serializers import VendorSerializer

# Create your views here.


class ProductCreationListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.ProductSerializer
    # parser_classes = [MultiPartParser]
    queryset = models.Product.objects.all()


class RetrieveDeleteUpdateProductView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    # parser_classes = [MultiPartParser]
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    # parser_classes = PageNumberPagination


class CreateProductImages(generics.CreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ProductImageSerializer
    parser_classes = [MultiPartParser]
    queryset = models.ProductImage.objects.all()


class RetrieveDeleteProductImages(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.ProductImageSerializer
    queryset = models.ProductImage.objects.all()


class ProductColorCreation(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.ProductColorSerializer
    queryset = models.Color.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        product = serializer.validated_data['product']
        color = serializer.validated_data['color']

        # Check if the color already exists for the given user and product
        if models.Color.objects.filter(user=user, product=product, color=color).exists():
            return Response({'message': 'Color already exists for this product.'}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DeleteProductColor(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.ProductColorSerializer
    queryset = models.Color.objects.all()


class GetProductColors(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, pk):
        product = models.Product.objects.get(id=pk)
        queryset = models.Color.objects.filter(product=product)
        serializer = serializers.ProductColorSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductSizeCreation(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.ProductSizeSerializer
    queryset = models.ProductSize.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        product = serializer.validated_data['product']
        size = serializer.validated_data['size']

        
        if models.ProductSize.objects.filter(user=user, product=product, size=size).exists():
            return Response({'message': 'Size already exists for this product.'}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DeleteProductSize(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.ProductSizeSerializer
    queryset = models.ProductSize.objects.all()


class GetProductSizes(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, pk):
        product = models.Product.objects.get(id=pk)
        queryset = models.ProductSize.objects.filter(product=product)
        serializer = serializers.ProductSizeSerializer(queryset, many=True)
        return Response(serializer.data)


class OrderCreationView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()


class RetrieveUpdateOrderView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()


class OrderItemCreationView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.OrderItemSerializer
    queryset = models.OrderItem.objects.all()


class RetrieveUpdateOrderView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.OrderItemSerializer
    queryset = models.OrderItem.objects.all()


class ProductReviewCreationView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.ProductReviewSerializer
    queryset = models.ProductReview.objects.all()


class GetProductReview(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, pk):
        product = models.Product.objects.get(id=pk)
        review = models.ProductReview.objects.filter(product=product)
        serializer = serializers.ProductReviewSerializer(review, many=True)
        return Response(serializer.data)


class RetrieveUpdateOrderView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.ProductReviewSerializer
    queryset = models.ProductReview.objects.all()


class WishListCreationView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.WishListSerializer
    queryset = models.Wishlist.objects.all()


class RemoveWishlist(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.WishListSerializer

    def delete(self, request, pk):
        try:
            product = models.Product.objects.get(id=pk)
            wishlist = models.Wishlist.objects.get(user=request.user, product=product)
            wishlist.delete()
            return Response({"response": "Wishlist item removed successfully"})
        except models.Wishlist.DoesNotExist:
            return Response({"response": "Wishlist item does not exist"}, status=404)


class CheckProductAsWishList(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.WishListSerializer

    def get(self, request, pk):
        try:
            product = models.Product.objects.get(id=pk)
            wishlist = models.Wishlist.objects.get(user=request.user, product=product)
            return Response({"response": "Product is added as wishlist"})
        except models.Wishlist.DoesNotExist:
            return Response({"response": "Wishlist item does not exist"}, status=404)


class GetUserWishList(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request):
        product = models.Wishlist.objects.filter(user=request.user)
        serializer = serializers.GetWishListSerializer(product, many=True)
        return Response(serializer.data)


class RetrieveUpdateOrderView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.WishListSerializer
    queryset = models.Wishlist.objects.all()


class SearchForProduct(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        q = self.request.query_params.get("q")
        if q:
            product = models.Product.objects.filter(
                Q(name__icontains=q)
                | Q(product_brand__icontains=q)
                | Q(product_category__icontains=q)
                | Q(vendor__shop_name__icontains=q)
            )
            return product


class SearchForVendor(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = VendorSerializer

    def get_queryset(self):
        q = self.request.query_params.get("q")
        if q:
            vendor = models.Vendor.objects.filter(
                Q(shop_name__icontains=q)
                | Q(region__icontains=q)
                | Q(address__icontains=q)
            )
            return vendor
