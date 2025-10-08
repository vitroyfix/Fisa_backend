from django.db import models
from django.utils import timezone

class Attend(models.Model):
    student = models.ForeignKey(
        "Student.Student",  #
        on_delete=models.CASCADE,
        related_name="attendances"
    )
    event = models.ForeignKey(
        "Events.Event",  
        on_delete=models.CASCADE,
        related_name="attendees"
    )

    registration_date = models.DateTimeField(
        default=timezone.now,
        help_text="When the student registered for the event"
    )
    attended_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text="The actual date/time when the student attended"
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ("attended", "Attended"),
            ("missed", "Missed"),
            ("cancelled", "Cancelled"),
        ],
        default="missed",
        help_text="Status of attendance"
    )
    feedback = models.TextField(
        blank=True,
        null=True,
        help_text="Optional feedback from the student about the event"
    )
    certificate_issued = models.BooleanField(
        default=False,
        help_text="Whether a certificate of participation was issued"
    )
    created_at = models.DateTimeField(auto_now_add=True)   
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('student', 'event')  
        verbose_name = "Attendance"
        verbose_name_plural = "Attendances"
        ordering = ['-created_at']

    def __str__(self):
        student_name = f"{self.student.admissions.first_name} {self.student.admissions.last_name}"
        return f"{student_name} - {self.event.title} ({self.status})"
