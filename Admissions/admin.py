from django.contrib import admin
from .models import Admissions

@admin.register(Admissions)
class AdmissionsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'reg_number', 'course')
    list_search = ('first_name', 'last_name')
    filter = ('first_name', 'last_name', 'reg_number', 'course')