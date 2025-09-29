from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_diaplay = ('title', 'description', 'location', 'time', 'speakers', 'partners')
    list_search = ('title', 'loaction')
    filter = ('title', 'location')
