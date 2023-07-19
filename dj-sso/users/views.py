from django.http import HttpResponse
from oauth2_provider.decorators import protected_resource


@protected_resource()
def protected_view(request):
    return HttpResponse("<h1>Protected Resource</h1>")
