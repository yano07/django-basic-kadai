from django.urls import path
from .views import TopView, ProductListView, ProductDetailView

urlpatterns = [
    path("", TopView.as_view(), name="top"),
    path("crud/", ProductListView.as_view(), name="product_list"),
    path("crud/detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]
