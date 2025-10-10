from django.db import models
from django.utils import timezone

class Student(models.Model):
    admissions = models.ForeignKey(
        "Admissions.Admission",
        on_delete=models.CASCADE,
        related_name="student_profile",
        help_text="The admission record associated with this student"
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
        return {
            "full_name": self.full_name,
            "email": self.admissions.email,
            "phone": self.admissions.phone_number,   
            "gender": self.admissions.gender,
            "dob": self.admissions.date_of_birth,    
            "admission_date": self.admissions.admission_date,
            "status": self.admissions.status,
        }

    @property
    def events_attended(self):
        return [attend.event for attend in self.attendances.all()]

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['admissions__first_name', 'admissions__last_name']
