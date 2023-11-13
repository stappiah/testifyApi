from django.urls import path
from . import views

urlpatterns = [
    path('vendor-registration', views.VendorCreationView.as_view()),
    path('vendor-details/<int:pk>', views.RetrieveUpdateVendorView.as_view()),
]
