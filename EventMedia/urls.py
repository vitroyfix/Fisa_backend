from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import MediaViewSet

router = DefaultRouter()
router.register(r'eventmedia', MediaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]