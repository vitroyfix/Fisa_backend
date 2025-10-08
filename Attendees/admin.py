from django.contrib import admin
from .models import Attend

@admin.register(Attend)
class AttendAdmin(admin.ModelAdmin):
    # Columns shown in the list view
    list_display = (
        'student_name',
        'event_name',
        'status',
        'registration_date',
        'attended_date',
        'certificate_issued',
        'created_at',
    )

    # Fields to search
    search_fields = (
        'student__admissions__first_name',
        'student__admissions__last_name',
        'student__admissions__reg_number',
        'event__title',
    )

    # Filters in sidebar
    list_filter = ('status', 'certificate_issued', 'event')

    # Default ordering
    ordering = ('-created_at',)

    # Fields editable directly in list view
    list_editable = ('status', 'certificate_issued')

    # Clickable links in list view
    list_display_links = ('student_name', 'event_name')

    # Fields read-only
    readonly_fields = ('created_at', 'updated_at')

    # Organize form layout
    fieldsets = (
        ("Student & Event", {
            "fields": ("student", "event")
        }),
        ("Attendance Details", {
            "fields": ("status", "registration_date", "attended_date")
        }),
        ("Feedback & Certification", {
            "fields": ("feedback", "certificate_issued")
        }),
        ("System Info", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)  # collapsible section
        }),
    )

    # Helper methods for list display
    def student_name(self, obj):
        if hasattr(obj.student, 'admissions'):
            return f"{obj.student.admissions.first_name} {obj.student.admissions.last_name}"
        return str(obj.student)
    student_name.short_description = "Student"

    def event_name(self, obj):
        return getattr(obj.event, 'title', str(obj.event))
    event_name.short_description = "Event"

    actions = ['mark_attended', 'mark_missed', 'issue_certificate']

    def mark_attended(self, request, queryset):
        updated = queryset.update(status='attended')
        self.message_user(request, f"{updated} attendance(s) marked as Attended.")
    mark_attended.short_description = "Mark selected as Attended"

    def mark_missed(self, request, queryset):
        updated = queryset.update(status='missed')
        self.message_user(request, f"{updated} attendance(s) marked as Missed.")
    mark_missed.short_description = "Mark selected as Missed"

    def issue_certificate(self, request, queryset):
        updated = queryset.update(certificate_issued=True)
        self.message_user(request, f"Certificates issued for {updated} attendance(s).")
    issue_certificate.short_description = "Issue Certificates for selected"
