from rest_framework.permissions import BasePermission
from config import env

class IsAuthServiceApplication(BasePermission):
    def has_permission(self, request, view):
        return request.auth and request.auth.application and \
          request.auth.application.client_id == env.SSO_SVC_CLIENT_ID
