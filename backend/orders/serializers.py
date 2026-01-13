from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'item_name_snapshot', 'price_snapshot', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    restaurant_name = serializers.ReadOnlyField(source='restaurant.name')

    class Meta:
        model = Order
        fields = [
            'id', 'order_number', 'restaurant_name', 'customer_phone',
            'delivery_address', 'payment_method', 'total_amount',
            'status', 'notes', 'created_at', 'items'
        ]
