from django.urls import path
from . import views

urlpatterns = [
    path('register', views.VendorCreationView.as_view()),
    path('vendor-details/<int:pk>', views.RetrieveUpdateVendorView.as_view()),
    path('user-shop', views.GetUserShops.as_view())
]
