from django.db import models
from django.utils import timezone

class Admissions(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=200)
    reg_number = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    year = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"({self.first_name}) ({self.last_name}) ({self.course})"
