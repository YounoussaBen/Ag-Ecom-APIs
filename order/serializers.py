from rest_framework import serializers
from .models import ShippingAddress, Order, OrderItem
from shop.serializers import ProductSerializer

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        exclude = ("is_deleted",)
        read_only_fields = ("created", "updated")


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    
    class Meta:
        model = OrderItem
        exclude = ("is_deleted",)
        read_only_fields = ("created", "updated")


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        exclude = ("is_deleted",)
        read_only_fields = ("created", "updated", "created_by")

