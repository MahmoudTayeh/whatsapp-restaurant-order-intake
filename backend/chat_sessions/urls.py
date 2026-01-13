from django.urls import path
from .views import WhatsAppWebhookView

urlpatterns = [
    path('webhook/whatsapp/', WhatsAppWebhookView.as_view(), name='whatsapp_webhook'),
]
