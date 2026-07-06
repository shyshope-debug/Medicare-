from django.contrib import admin
from django.urls import path, include
from . import whatsapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pharmacy.urls')),
    path('whatsapp/', whatsapp.whatsapp_webhook, name='whatsapp_webhook'),
]
