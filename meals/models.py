from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    preparation_time = models.PositiveIntegerField(help_text="Preparation time in minutes")
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return f"Recipe for {self.meal.name}"

class NutritionalInfo(models.Model):
    meal = models.OneToOneField(Meal, on_delete=models.CASCADE)
    calories = models.PositiveIntegerField()
    fat = models.DecimalField(max_digits=5, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=5, decimal_places=2)
    protein = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Nutritional Info for {self.meal.name}"