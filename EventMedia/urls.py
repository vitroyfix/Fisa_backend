from django.urls import path
from .views import media_list_view

urlpatterns = [
    path('', media_list_view, name='media_list'),
]
