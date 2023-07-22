from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('sso/admin/', admin.site.urls),
    path('sso/o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('sso/api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('sso/', include('users.urls'), name='users'),
]
