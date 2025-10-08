from django.contrib import admin
from .models import NonMember

@admin.register(NonMember)
class NonMemberAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "institution",
        "email",
        "status",
        "certificate_issued",
        "created_at"
    )
    search_fields = ("first_name", "last_name", "institution", "email")
    list_filter = ("status", "certificate_issued", "events")
    filter_horizontal = ("events",)
    list_editable = ("status", "certificate_issued")
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Personal Info", {
            "fields": ("first_name", "last_name", "email", "phone_number", "institution")
        }),
        ("Event Participation", {
            "fields": ("events", "status", "registration_date", "attended_date")
        }),
        ("Feedback & Certification", {
            "fields": ("feedback", "certificate_issued")
        }),
        ("System Info", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )
