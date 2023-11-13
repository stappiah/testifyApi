from django.urls import path
from . import views

urlpatterns = [
    path('product', views.ProductCreationListView.as_view()),
    path('product-detail/<int:pk>',
         views.RetrieveDeleteUpdateProductView.as_view()),
    path('colors', views.GetProductColors.as_view()),
    path('product-image', views.CreateProductImages.as_view()),
    path('product-image/<int:pk>', views.RetrieveDeleteProductImages.as_view()),
]
