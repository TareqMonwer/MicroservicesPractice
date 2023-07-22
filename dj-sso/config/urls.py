from rest_framework_simplejwt import views as jwt_views

from django.contrib import admin
from django.urls import path, include
# from users.views.user_primary_views import protected_view


urlpatterns = [
    path('sso/admin/', admin.site.urls),
    # path('sso/', protected_view, name='protected_view'),
    path('sso/auth/', jwt_views.TokenObtainPairView.as_view(), name='authentication'),
    path('sso/auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='authentication_refresh'),
    path('sso/o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('sso/api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('sso/', include('users.urls'), name='users'),
]
