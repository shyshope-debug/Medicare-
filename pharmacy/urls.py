from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import PatientViewSet, DrugViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'drugs', DrugViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
