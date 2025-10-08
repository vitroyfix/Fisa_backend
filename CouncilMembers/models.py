from django.db import models
from django.utils import timezone

class Council(models.Model):
    student = models.ForeignKey(
        "Student.Student",
        on_delete=models.CASCADE,
        related_name="council_positions"
    )
    role_position = models.CharField(
        max_length=200,
        help_text="The role or position of the student in the council"
    )
    committee = models.CharField(
        max_length=200,
        help_text="The committee the student belongs to"
    )
    start_date = models.DateField(
        default=timezone.now,
        help_text="The date the student started this council role"
    )
    end_date = models.DateField(
        null=True,
        blank=True,
        help_text="The date the student ended this council role (if applicable)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Council Member"
        verbose_name_plural = "Council Members"
        ordering = ["committee", "role_position", "student"]

    def __str__(self):
        return f"{self.student} - {self.role_position} ({self.committee})"
