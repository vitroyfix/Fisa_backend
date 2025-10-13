from django.contrib import admin
from .models import Media, PersonalMedia


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "media_type", "created_at")
    list_filter = ("category", "media_type", "created_at")
    search_fields = ("title", "category")
    ordering = ("-created_at",)


@admin.register(PersonalMedia)
class PersonalMediaAdmin(admin.ModelAdmin):
    list_display = ("student", "image", "created_at")
    readonly_fields = ("student", "image", "created_at", "updated_at")
    ordering = ("-created_at",)

    def has_add_permission(self, request):
        return False 

    def has_change_permission(self, request, obj=None):
        return False  

    def has_delete_permission(self, request, obj=None):
        return True 