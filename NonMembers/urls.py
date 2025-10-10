from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NonMemberViewSet

router = DefaultRouter()
router.register(r'nonmembers', NonMemberViewSet, basename='nonmember')

urlpatterns = [
    path('', include(router.urls)),
]
