from django.contrib import admin
from .models import NonMember

@admin.register(NonMember)
class NonMemberAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "institution")
    search_fields = ("first_name", "last_name", "institution")
    filter_horizontal = ("events",)  # Better UI for selecting multiple events
