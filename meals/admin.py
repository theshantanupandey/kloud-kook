from django.contrib import admin
from .models import Meal, Recipe, NutritionalInfo

class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 1

class NutritionalInfoInline(admin.StackedInline):
    model = NutritionalInfo
    extra = 1

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    inlines = (RecipeInline, NutritionalInfoInline)
    list_display = ('name', 'price', 'preparation_time', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('name',)
    actions = ['mark_as_available', 'mark_as_unavailable']

    def mark_as_available(self, request, queryset):
        queryset.update(is_available=True)
    mark_as_available.short_description = "Mark selected meals as available"

    def mark_as_unavailable(self, request, queryset):
        queryset.update(is_available=False)
    mark_as_unavailable.short_description = "Mark selected meals as unavailable"