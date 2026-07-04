from django.contrib import admin
from django.urls import path, include
from pharmacy.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # adds login/logout/password reset
    path('', home, name='home'),
]
