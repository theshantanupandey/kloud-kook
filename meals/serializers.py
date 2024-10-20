from rest_framework import serializers
from .models import Meal, Recipe, NutritionalInfo

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('ingredients', 'instructions')

class NutritionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionalInfo
        fields = ('calories', 'fat', 'carbohydrates', 'protein')

class MealSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer()
    nutritional_info = NutritionalInfoSerializer()

    class Meta:
        model = Meal
        fields = ('id', 'name', 'description', 'price', 'preparation_time', 'is_available', 'recipe', 'nutritional_info')