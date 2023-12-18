from django.urls import path
from . import views

urlpatterns = [
    path("", views.GetVendors.as_view()),
    path("register", views.VendorCreationView.as_view()),
    path("details/<int:pk>", views.RetrieveUpdateVendorView.as_view()),
    path("user-shop", views.GetUserShops.as_view()),
    path("product/<int:pk>", views.GetVendorProducts.as_view()),
    path("follow-vendor", views.FollowVendor.as_view()),
    path("check-follower/<int:pk>", views.CheckVendorFollower.as_view()),
    path("unfollow-vendor/<int:pk>", views.UnFollowVendor.as_view()),
    path("search-vendor-product/<int:pk>", views.SearchVendorProduct.as_view()),
    path("average-rating/<int:pk>", views.VendorAverageRating.as_view()),
    path("rating", views.VendorReviewCreation.as_view()),
    path("rating/<int:pk>", views.GetVendorReview.as_view()),
]
