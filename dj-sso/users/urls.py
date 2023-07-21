from django.urls import include, path
from users.views import UserPrimaryViewSet
from rest_framework import routers


users_router = routers.DefaultRouter()
users_router.register(r'users', UserPrimaryViewSet)

urlpatterns = [
    path('', include(users_router.urls)),
]