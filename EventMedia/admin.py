from django.contrib import admin
from .models import Media

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "media_type", "media_file")
    search_fields = ("title", "category")
    list_filter = ("category", "media_type")
