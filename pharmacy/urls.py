from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('webhook/', views.whatsapp_webhook, name='whatsapp_webhook'),
]
