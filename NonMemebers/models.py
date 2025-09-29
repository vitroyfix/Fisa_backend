from django.db import models

class NonMember(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    events = models.ManyToManyField("Events.Event", related_name="non_members")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.institution})"
