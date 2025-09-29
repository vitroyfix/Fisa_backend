from django.db import models
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=False, blank=False)
    location = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now)
    speakers = models.JSONField(default=list) 
    partners = models.JSONField(default=list)

    def __str__ (self):
        return f"({self.title}) ({self.location}) ({self.time})"