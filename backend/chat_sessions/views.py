from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import InboundMessage, ConversationSession
from restaurants.models import RestaurantChannel
import logging

logger = logging.getLogger(__name__)

class WhatsAppWebhookView(APIView):
    def post(self, request, *args, **kwargs):
        payload = request.data
        
        # Basic validation of payload structure (provider dependent)
        # For MVP, we assume a generic structure
        try:
            message_id = payload.get("id")
            sender_phone = payload.get("from")
            receiver_id = payload.get("to")
            text = payload.get("text", {}).get("body", "")
            
            if not all([message_id, sender_phone, receiver_id]):
                return Response({"error": "Invalid payload"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Idempotency check
            if InboundMessage.objects.filter(provider_message_id=message_id).exists():
                return Response({"status": "already processed"}, status=status.HTTP_200_OK)
            
            # Log inbound message
            InboundMessage.objects.create(
                provider_message_id=message_id,
                sender_phone=sender_phone,
                receiver_identifier=receiver_id,
                message_text=text,
                raw_payload=payload
            )
            
            # Identify restaurant
            try:
                channel = RestaurantChannel.objects.get(inbound_identifier=receiver_id, is_active=True)
                restaurant = channel.restaurant
            except RestaurantChannel.DoesNotExist:
                logger.warning(f"Unknown inbound identifier: {receiver_id}")
                return Response({"status": "unknown restaurant"}, status=status.HTTP_200_OK)
            
            # Get or create session
            session, created = ConversationSession.objects.get_or_create(
                restaurant=restaurant,
                customer_phone=sender_phone,
                defaults={"state": "START"}
            )
            
            # Process message through state machine (to be implemented)
            # For now, just return success
            return Response({"status": "received"}, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Error processing webhook: {str(e)}")
            return Response({"error": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, *args, **kwargs):
        # Verification for Meta WhatsApp Cloud API
        verify_token = "YOUR_VERIFY_TOKEN" # Should be in settings
        mode = request.query_params.get("hub.mode")
        token = request.query_params.get("hub.verify_token")
        challenge = request.query_params.get("hub.challenge")
        
        if mode and token:
            if mode == "subscribe" and token == verify_token:
                return Response(int(challenge), status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)
