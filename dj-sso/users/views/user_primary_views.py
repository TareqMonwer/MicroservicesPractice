from oauth2_provider.decorators import protected_resource
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from users.permissions import IsAuthServiceApplication
from users.serializers import UserPrimarySerializer
from users.models import User

class UserPrimaryViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated & IsAuthServiceApplication]
    permission_classes = [IsAuthenticated, ]
    queryset = User.objects.all()
    serializer_class = UserPrimarySerializer


@protected_resource()
def protected_view(request):
    return HttpResponse("<h1>Protected Resource</h1>")
