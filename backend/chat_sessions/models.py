from django.db import models
from restaurants.models import Restaurant

class ConversationSession(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    customer_phone = models.CharField(max_length=20)
    state = models.CharField(max_length=50, default="START")
    context = models.JSONField(default=dict)
    last_activity = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ("restaurant", "customer_phone")

    def __str__(self):
        return f"{self.customer_phone} @ {self.restaurant.name} ({self.state})"

class InboundMessage(models.Model):
    provider_message_id = models.CharField(max_length=255, unique=True)
    sender_phone = models.CharField(max_length=20)
    receiver_identifier = models.CharField(max_length=100)
    message_text = models.TextField()
    raw_payload = models.JSONField()
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Msg {self.provider_message_id} from {self.sender_phone}"
