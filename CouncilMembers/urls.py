from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CouncilViewSet

router = DefaultRouter()
router.register(r'councils', CouncilViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
