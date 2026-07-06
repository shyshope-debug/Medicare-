from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order/<int:medicine_id>/', views.order_medicine, name='order_medicine'),
]
