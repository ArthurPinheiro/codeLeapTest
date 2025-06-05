from rest_framework.routers import DefaultRouter
from .views import CareerViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'', CareerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]