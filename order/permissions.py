from rest_framework import permissions
from order.models import Order

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print("Afadf")
        if request.user.is_staff:
            return True
        return obj.shipper.user == request.user

    

class IsDriver(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False


        order_id = view.kwargs.get('pk')

        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return False

        if hasattr(request.user, 'driver') :
           
            return True

        return False

class IsCompanyEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if hasattr(request.user, 'companyemployee') :
           
            return True

        return False
    
class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.role == 'superuser':
            return True
        return False    
