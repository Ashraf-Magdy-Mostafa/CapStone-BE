from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Product, Order
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    OrderCreateSerializer,
    OrderSerializer,
)


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "description", "category__name"]
    ordering_fields = ["price", "rating", "stock", "id"]
    ordering = ["-id"]

    def get_queryset(self):
        qs = Product.objects.select_related("category").all()
        category_slug = self.request.query_params.get("category")
        in_stock = self.request.query_params.get("in_stock")
        min_price = self.request.query_params.get("min_price")
        max_price = self.request.query_params.get("max_price")

        if category_slug:
            qs = qs.filter(category__slug=category_slug)
        if in_stock in ("1", "true", "True"):
            qs = qs.filter(stock__gt=0)
        if min_price:
            qs = qs.filter(price__gte=min_price)
        if max_price:
            qs = qs.filter(price__lte=max_price)
        return qs


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.select_related("category").all()
    serializer_class = ProductSerializer
    lookup_field = "id"


class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        return Response(OrderSerializer(order).data, status=201)


class OrderDetailAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.prefetch_related("items__product__category").all()
    serializer_class = OrderSerializer
    lookup_field = "id"


class HealthAPIView(APIView):
    def get(self, request):
        return Response({"status": "ok"})
