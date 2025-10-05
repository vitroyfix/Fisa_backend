from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendances_view, name='attendees'),
]
