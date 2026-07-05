from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Medicare is online. /admin to login")

urlpatterns = [
    path('', home),  # This fixes the shutdown issue
    path('admin/', admin.site.urls),
]
