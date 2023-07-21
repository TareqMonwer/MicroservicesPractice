from oauth2_provider.contrib.rest_framework import TokenHasResourceScope
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAuthServiceApplication
from users.serializers import UserPrimarySerializer
from users.models import User

class UserPrimaryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & IsAuthServiceApplication]
    queryset = User.objects.all()
    serializer_class = UserPrimarySerializer
    
