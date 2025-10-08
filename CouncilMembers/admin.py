from django.contrib import admin
from .models import Council

@admin.register(Council)
class CouncilAdmin(admin.ModelAdmin):
    list_display = (
        'student_full_name',
        'role_position',
        'committee',
        'start_date',
        'end_date',
        'created_at'
    )
    search_fields = (
        'student__admissions__first_name',
        'student__admissions__last_name',
        'role_position',
        'committee'
    )
    list_filter = ('committee', 'role_position', 'start_date', 'end_date')
    ordering = ('student__admissions__first_name', 'student__admissions__last_name')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ("Student Info", {
            "fields": ("student",)
        }),
        ("Council Role", {
            "fields": ("role_position", "committee", "start_date", "end_date")
        }),
        ("System Info", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )

    def student_full_name(self, obj):
        return f"{obj.student.admissions.first_name} {obj.student.admissions.last_name}"
    student_full_name.short_description = 'Student Name'
