from rest_framework import viewsets, permissions
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Ensure staff only see orders for their restaurant
        # For MVP, we assume staff is linked to a restaurant via a profile (to be added)
        # For now, return all orders but filter by restaurant if provided in query
        queryset = Order.objects.all().order_by("-created_at")
        restaurant_id = self.request.query_params.get("restaurant_id")
        if restaurant_id:
            queryset = queryset.filter(restaurant_id=restaurant_id)
        return queryset
