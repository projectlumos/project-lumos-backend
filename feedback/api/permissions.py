from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerFeedback(BasePermission):
    message = "You must be the owner of the object to view."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            if obj.user == None:
                # if user is anonymous then read-only
                return True

            # Check permissions for read-only request
            elif obj.user == request.user:
                return True
        else:
            # Check permissions for write request
            if obj.user == request.user:
                return True
