from rest_framework import serializers
from .models import Ingredient, Supplier

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'quantity', 'unit', 'reorder_level', 'expiration_date')

class SupplierSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Supplier
        fields = ('id', 'name', 'contact_info', 'ingredients')