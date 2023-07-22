"""
URL configuration for publisher_config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import requests

from oauth2_provider.views.generic import ProtectedResourceView
from oauth2_provider.decorators import protected_resource

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib import admin
from django.http import HttpResponse, JsonResponse
from django.urls import path

from utils.http_client import http_client
from . import env


def home(request):
    api_url = 'http://localhost:8001/publisher-service/services/'
    response = http_client.get(api_url)
    print(">>>>>>>>>>>>>>>")
    print(response, response.text)
    return HttpResponse("Publisher-Service")


# @protected_resource()
# def services(request):
#     # services = ["Book publishing", "Reviewing books", "Editorial support", "Cover designing"]
#     # return JsonResponse({'data': services})
#     if request.user.is_authenticated:
#         # Return the protected data as a JSON response.
#         data = {"message": "This is a protected resource accessible only to authenticated users."}
#         return JsonResponse(data)
#     else:
#         # Return a 401 Unauthorized response if the user is not authenticated.
#         return JsonResponse({"message": "Authentication required."}, status=401)


class ProtectedServices(APIView):
    permission_classes = (IsAuthenticated, )
  
    def get(self, request):
        content = {'message': 'Hello, GeeksforGeeks'}
        return Response(content)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('publisher-service/', home),
    path('publisher-service/services/', ProtectedServices.as_view()),
]
