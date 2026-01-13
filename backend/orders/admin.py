from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("item_name_snapshot", "price_snapshot", "quantity")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_number", "restaurant", "customer_phone", "total_amount", "status", "created_at")
    list_filter = ("status", "restaurant")
    search_fields = ("order_number", "customer_phone")
    inlines = [OrderItemInline]
