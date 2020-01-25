from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Lets user edit their own profiles"""

    def has_object_permission(self,request,view,obj):
        """ Check  if user is trying to edit htier own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):
    """ Lets user update thier own status and not somebody else's"""


    def has_object_permission(self,request,view,obj):
        """ check if the current user is trying to edit thier own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id