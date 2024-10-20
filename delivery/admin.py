from django.contrib import admin
from .models import Delivery

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('order', 'delivery_person', 'status', 'delivery_time')
    list_filter = ('status', 'delivery_time')
    search_fields = ('order__id', 'delivery_person__username')