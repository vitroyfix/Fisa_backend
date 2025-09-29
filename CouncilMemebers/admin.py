from django.contrib import admin
from .models import Council

@admin.register(Council)
class CouncilAdmin(admin.ModelAdmin):
    list_display = ('student_full_name', 'role_position', 'committee')
    search_fields = ('student__admissions__first_name', 'student__admissions__last_name', 'role_position')
    ordering = ('student__admissions__first_name', 'student__admissions__last_name')

    
    def student_full_name(self, obj):
        return f"{obj.student.admissions.first_name} {obj.student.admissions.last_name}"
    
    student_full_name.short_description = 'Student Name'
