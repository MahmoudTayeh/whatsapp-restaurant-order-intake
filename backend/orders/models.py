from django.db import models
from restaurants.models import Restaurant, MenuItem

class Order(models.Model):
    STATUS_CHOICES = [
        ("NEW", "New"),
        ("ACCEPTED", "Accepted"),
        ("PREPARING", "In Preparation"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    ]

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="orders")
    order_number = models.CharField(max_length=20)
    customer_phone = models.CharField(max_length=20)
    delivery_address = models.TextField()
    payment_method = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="NEW")
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.order_number} - {self.restaurant.name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    menu_item = models.ForeignKey(MenuItem, on_delete=models.SET_NULL, null=True)
    item_name_snapshot = models.CharField(max_length=255)
    price_snapshot = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.item_name_snapshot}"
