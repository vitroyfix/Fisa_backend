from django.contrib import admin
from .models import Student
from Attendees.models import Attend  # Assuming Attend model is in Attendees app

class AttendInline(admin.TabularInline):
    model = Attend
    extra = 0
    readonly_fields = ('event', 'registration_date', 'attended_date', 'status', 'certificate_issued')
    can_delete = False
    verbose_name = "Event Attendance"
    verbose_name_plural = "Event Attendances"

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'reg_number', 'course', 'phone_number')
    search_fields = ('admissions__first_name', 'admissions__last_name', 'admissions__reg_number', 'admissions__course')
    list_filter = ('admissions__course',)  # Optional if course exists
    inlines = [AttendInline]

    def full_name(self, obj):
        return f"{obj.admissions.first_name} {obj.admissions.last_name}"
    
    def reg_number(self, obj):
        return obj.admissions.reg_number
    
    def course(self, obj):
        return obj.admissions.course
    
    def phone_number(self, obj):
        return obj.admissions.phone_number
