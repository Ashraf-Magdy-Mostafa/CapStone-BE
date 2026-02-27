from django.urls import path
from .views import (
    HealthAPIView,
    CategoryListAPIView,
    ProductListAPIView,
    ProductDetailAPIView,
    OrderCreateAPIView,
    OrderDetailAPIView,
)

urlpatterns = [
    path("health/", HealthAPIView.as_view()),
    path("categories/", CategoryListAPIView.as_view()),
    path("products/", ProductListAPIView.as_view()),
    path("products/<int:id>/", ProductDetailAPIView.as_view()),
    path("orders/", OrderCreateAPIView.as_view()),
    path("orders/<int:id>/", OrderDetailAPIView.as_view()),
]
