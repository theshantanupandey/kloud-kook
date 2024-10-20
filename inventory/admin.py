from django.contrib import admin
from .models import Ingredient, Supplier

class SupplierInline(admin.TabularInline):
    model = Supplier.ingredients.through
    extra = 1

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    inlines = (SupplierInline,)
    list_display = ('name', 'quantity', 'unit', 'reorder_level', 'expiration_date')
    list_filter = ('unit', 'expiration_date')
    search_fields = ('name',)
    actions = ['increase_quantity', 'decrease_quantity']

    def increase_quantity(self, request, queryset):
        for ingredient in queryset:
            ingredient.quantity += 10
            ingredient.save()
    increase_quantity.short_description = "Increase quantity by 10"

    def decrease_quantity(self, request, queryset):
        for ingredient in queryset:
            if ingredient.quantity >= 10:
                ingredient.quantity -= 10
                ingredient.save()
    decrease_quantity.short_description = "Decrease quantity by 10"