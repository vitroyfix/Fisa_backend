from django.db import models

class Attend(models.Model):
    student = models.ForeignKey("Student.Student", on_delete=models.CASCADE)
    event = models.ForeignKey("Events.Event", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} attended {self.event}"
