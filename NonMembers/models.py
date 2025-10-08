from django.db import models
from django.utils import timezone

class NonMember(models.Model):
    STATUS_CHOICES = [
        ("registered", "Registered"),
        ("attended", "Attended"),
        ("cancelled", "Cancelled"),
    ]

    # Personal info
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    institution = models.CharField(max_length=200)
    
    # Event participation
    events = models.ManyToManyField(
        "Events.Event", 
        related_name="non_members"
    )
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default="registered",
        help_text="Current participation status"
    )
    registration_date = models.DateTimeField(
        default=timezone.now,
        help_text="Date when the non-member registered for the event"
    )
    attended_date = models.DateTimeField(
        blank=True, null=True,
        help_text="Date when the non-member actually attended"
    )

    # Additional info
    feedback = models.TextField(blank=True, null=True)
    certificate_issued = models.BooleanField(default=False)

    # System fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Non-Member"
        verbose_name_plural = "Non-Members"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.institution})"
