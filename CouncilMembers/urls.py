from django.urls import path
from . import views

urlpatterns = [
    path('', views.council_view, name='council'),
]
