from django.urls import path
from . import views

urlpatterns = [
    path('', views.admissions_view, name='admissions'),
]
