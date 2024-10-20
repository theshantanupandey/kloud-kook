from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=50)
    reorder_level = models.PositiveIntegerField(default=10)
    expiration_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit})"

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, related_name='suppliers')

    def __str__(self):
        return self.name