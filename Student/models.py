from django.db import models

class Student(models.Model):
    admissions = models.ForeignKey("Admissions.Admissions", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.admissions.first_name} {self.admissions.last_name}"
