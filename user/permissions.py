
from rest_framework.permissions import BasePermission

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'user_type') and request.user.user_type == 'customer'

class IsRepairer(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'user_type') and request.user.user_type == 'repairer'
