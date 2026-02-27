from rest_framework import serializers
from .models import Category, Product, Order, OrderItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "category",
            "category_id",
            "name",
            "slug",
            "description",
            "price",
            "stock",
            "rating",
            "image_url",
        ]

class OrderItemWriteSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)

class OrderItemReadSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity", "unit_price", "line_total"]

class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemWriteSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "full_name",
            "email",
            "phone",
            "address_line1",
            "address_line2",
            "city",
            "country",
            "postal_code",
            "items",
        ]

    def create(self, validated_data):
        from decimal import Decimal
        from .models import Product

        items_data = validated_data.pop("items", [])
        order = Order.objects.create(**validated_data)

        subtotal = Decimal("0")
        for item in items_data:
            product = Product.objects.get(id=item["product_id"])
            qty = int(item["quantity"])
            unit_price = product.price
            line_total = unit_price * qty
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=qty,
                unit_price=unit_price,
                line_total=line_total,
            )
            subtotal += line_total

            # reduce stock (simple demo behavior)
            if product.stock >= qty:
                product.stock -= qty
                product.save(update_fields=["stock"])

        # simple shipping rule: free shipping over 2000 EGP, else 75 EGP
        shipping = Decimal("0") if subtotal >= Decimal("2000") else Decimal("75")
        total = subtotal + shipping

        order.subtotal = subtotal
        order.shipping = shipping
        order.total = total
        order.save(update_fields=["subtotal", "shipping", "total"])
        return order

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemReadSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "full_name",
            "email",
            "phone",
            "address_line1",
            "address_line2",
            "city",
            "country",
            "postal_code",
            "status",
            "subtotal",
            "shipping",
            "total",
            "items",
            "created_at",
        ]
