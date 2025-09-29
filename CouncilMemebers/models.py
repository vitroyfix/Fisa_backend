from django.db import models

class Council(models.Model):
    student = models.ForeignKey("Student.Student", on_delete=models.CASCADE)
    role_position = models.CharField(max_length=200)
    committee = models.CharField(max_length=200)

    def __str__(self):
        return f"({self.student}) ({self.role_position}) ({self.committee})"

