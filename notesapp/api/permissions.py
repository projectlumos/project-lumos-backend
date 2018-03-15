from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwner(BasePermission):
    message = "You must be the owner of the object to view."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            # Checking whether the user is owner of the object
            if obj.user == request.user:
                return True
        else:
        	if obj.user == request.user:
        		return True
