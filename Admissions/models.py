from django.db import models
from django.utils import timezone

class Admission(models.Model):
    # Student personal info
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    reg_number = models.CharField(max_length=50, unique=True)
    
    # Academic details
    course = models.CharField(max_length=200)
    year_of_study = models.IntegerField(blank=True, null=True)
    admission_date = models.DateField(default=timezone.now)
    
    # Extra details
    gender = models.CharField(max_length=10, choices=[
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ], blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    # Process info
    status = models.CharField(max_length=20, choices=[
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ], default="pending")
    comments = models.TextField(blank=True, null=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.course} ({self.status})"
