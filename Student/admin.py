from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'reg_number', 'course', 'phone_number')

    def full_name(self, obj):
        return f"{obj.admissions.first_name} {obj.admissions.last_name}"
    
    def reg_number(self, obj):
        return obj.admissions.reg_number
    
    def course(self, obj):
        return obj.admissions.course
    
    def phone_number(self, obj):
        return obj.admissions.phone_number
