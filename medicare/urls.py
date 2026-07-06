from django.contrib import admin
from django.urls import path, include
from . import whatsapp
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pharmacy.urls')),
    path('track/', views.track_order, name='track_order'),
    path('whatsapp/', whatsapp.whatsapp_webhook, name='whatsapp_webhook'),
]
