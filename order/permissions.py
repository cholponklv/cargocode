from rest_framework import permissions
from order.models import Order

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.shipper.user == request.user
    

class IsDriverFromSameCity(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False


        order_id = view.kwargs.get('pk')

        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return False

        if hasattr(request.user, 'driver') and request.user.driver.city == order.location_city:
            print(request.user.driver.city)
            print(order.location_city)
            return True

        return False
