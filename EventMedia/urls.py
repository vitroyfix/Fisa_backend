from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MediaViewSet, PersonalMediaViewSet

router = DefaultRouter()
router.register(r"media", MediaViewSet, basename="media")
router.register(r"personalmedia", PersonalMediaViewSet, basename="personalmedia")

urlpatterns = [
    path("", include(router.urls)),
]
