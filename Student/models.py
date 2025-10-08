from django.db import models
from django.utils import timezone

class Student(models.Model):
    admissions = models.ForeignKey(
        "Admissions.Admission",
        on_delete=models.CASCADE,
        related_name="student_profile"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.admissions.first_name} {self.admissions.last_name}"

    @property
    def full_name(self):
        return f"{self.admissions.first_name} {self.admissions.last_name}"

    @property
    def details(self):
        """Return full admission details"""
        return {
            "full_name": self.full_name,
            "email": self.admissions.email,
            "phone": self.admissions.phone,
            "gender": self.admissions.gender,
            "dob": self.admissions.dob,
            "admission_date": self.admissions.admission_date,
            "status": self.admissions.status,
        }

    @property
    def events_attended(self):
        """Return all events this student has attended"""
        return [attend.event for attend in self.attendances.all()]
