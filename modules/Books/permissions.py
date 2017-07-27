from rest_framework import permissions

class GerardoPermmission(permissions.BasePermission):
    message= "No eres lo suficientemente genial para acceder."

    def hashpermission(self,request,view):

        if request.method == "GET" and request.user.email == "gerardo@gmail":
            return True
        else:
            return False