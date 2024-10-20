from django.contrib import admin
from .models import Order, OrderItem
from django.core.mail import send_mail

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemInline,)
    list_display = ('id', 'user', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('user__username', 'user__email')
    actions = ['mark_as_processing', 'mark_as_completed', 'mark_as_cancelled', 'send_order_notification']

    def mark_as_processing(self, request, queryset):
        queryset.update(status='processing')
    mark_as_processing.short_description = "Mark selected orders as processing"

    def mark_as_completed(self, request, queryset):
        queryset.update(status='completed')
    mark_as_completed.short_description = "Mark selected orders as completed"

    def mark_as_cancelled(self, request, queryset):
        queryset.update(status='cancelled')
    mark_as_cancelled.short_description = "Mark selected orders as cancelled"

    def send_order_notification(self, request, queryset):
        for order in queryset:
            send_mail(
                'Order Update',
                f'Your order #{order.id} status has been updated to {order.status}.',
                'from@example.com',
                [order.user.email],
                fail_silently=False,
            )
    send_order_notification.short_description = "Send order notification to users"