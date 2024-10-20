from django.core.management.base import BaseCommand
from inventory.models import Ingredient
from datetime import timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = 'Checks inventory levels and expiration dates'

    def handle(self, *args, **kwargs):
        ingredients = Ingredient.objects.all()
        for ingredient in ingredients:
            if ingredient.quantity < ingredient.reorder_level:
                self.stdout.write(self.style.WARNING(f"Reorder {ingredient.name}"))
            if ingredient.expiration_date and ingredient.expiration_date <= timezone.now().date() + timedelta(days=7):
                self.stdout.write(self.style.WARNING(f"Expiring soon: {ingredient.name}"))