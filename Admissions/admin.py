from django.contrib import admin
from .models import Admission

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = (
        "reg_number",
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "course",
        "year_of_study",
        "status",
        "admission_date",
        "created_at",
    )

    search_fields = ("first_name", "last_name", "email", "reg_number")

    list_filter = ("course", "status", "year_of_study", "admission_date")

    ordering = ("-created_at",)

    list_editable = ("status", "year_of_study", "course")

    list_display_links = ("reg_number", "first_name", "last_name")

    fieldsets = (
        ("Personal Info", {
            "fields": ("first_name", "middle_name", "last_name", "gender", "date_of_birth")
        }),
        ("Contact Details", {
            "fields": ("email", "phone_number", "address")
        }),
        ("Academic Info", {
            "fields": ("reg_number", "course", "year_of_study", "admission_date", "status")
        }),
        ("Additional", {
            "fields": ("comments",)
        }),
        ("System Info", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",), 
        }),
    )

    readonly_fields = ("created_at", "updated_at")

    actions = ["mark_as_approved", "mark_as_rejected", "mark_as_pending"]

    def mark_as_approved(self, request, queryset):
        queryset.update(status="approved")
    mark_as_approved.short_description = "Mark selected admissions as Approved"

    def mark_as_rejected(self, request, queryset):
        queryset.update(status="rejected")
    mark_as_rejected.short_description = "Mark selected admissions as Rejected"

    def mark_as_pending(self, request, queryset):
        queryset.update(status="pending")
    mark_as_pending.short_description = "Mark selected admissions as Pending"
