from django.urls import path
from . import views

urlpatterns = [
    path("product", views.ProductCreationListView.as_view()),
    path("product-detail/<int:pk>", views.RetrieveDeleteUpdateProductView.as_view()),
    path("product-image", views.CreateProductImages.as_view()),
    path("product-image/<int:pk>", views.RetrieveDeleteProductImages.as_view()),
    path("product-size", views.ProductSizeCreation.as_view()),
    path("retrieve-product-size/<int:pk>", views.GetProductSizes.as_view()),
    path("delete-product-size/<int:pk>", views.DeleteProductSize.as_view()),
    path("product-color", views.ProductColorCreation.as_view()),
    path("delete-color/<int:pk>", views.DeleteProductColor.as_view()),
    path("retrieve-color/<int:pk>", views.GetProductColors.as_view()),
]
