from django.shortcuts import render
from . import serializers
from . import models
from rest_framework import permissions, authentication, generics, response
from rest_framework.parsers import MultiPartParser
from rest_framework.request import Request
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

# Create your views here.


class ProductCreationListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.ProductSerializer
    parser_classes = [MultiPartParser]
    queryset = models.Product.objects.all()


class RetrieveDeleteUpdateProductView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    parser_classes = [MultiPartParser]
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


class RetrieveUpdateOrderView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = serializers.WishListSerializer
    queryset = models.Wishlist.objects.all()
