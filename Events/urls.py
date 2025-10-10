from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, CouncilEventParticipationViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'council-participations', CouncilEventParticipationViewSet, basename='council-participation')

urlpatterns = [
    path('', include(router.urls)),
]
