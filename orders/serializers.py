from rest_framework import serializers
from .models import Order, OrderItem
from meals.serializers import MealSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    meal = MealSerializer()

    class Meta:
        model = OrderItem
        fields = ('meal', 'quantity')

class OrderSerializer(serializers.ModelSerializer):
    meals = OrderItemSerializer(source='orderitem_set', many=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'meals', 'status', 'created_at', 'updated_at')