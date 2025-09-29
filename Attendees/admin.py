from django.contrib import admin
from .models import Attend

@admin.register(Attend)
class AttendAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'event_name')   
    search_fields = ('student__adminssions__first_name', 'student__adminssions__last_name', 'event__title')   
    list_filter = ('event',)   

    def student_name(self, obj):
        return f"{obj.student.adminssions.first_name} {obj.student.adminssions.last_name}"
    student_name.short_description = "Student"

    def event_name(self, obj):
        return obj.event.title
    event_name.short_description = "Event"
