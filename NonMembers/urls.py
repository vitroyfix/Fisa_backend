from django.urls import path
from . import views

urlpatterns = [
    path('', views.nonmembers_view, name='nonmembers'),
]
