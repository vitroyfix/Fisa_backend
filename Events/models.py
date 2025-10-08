from django.db import models
from django.utils import timezone


class Event(models.Model):
    EVENT_STATUS_CHOICES = [
        ("upcoming", "Upcoming"),
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    title = models.CharField(max_length=200, help_text="Event title")
    description = models.TextField(help_text="Detailed description of the event")
    location = models.CharField(max_length=200, help_text="Event location")
    time = models.DateTimeField(default=timezone.now, help_text="Start date and time of the event")
    end_time = models.DateTimeField(null=True, blank=True, help_text="End date and time of the event")
    speakers = models.JSONField(default=list, blank=True, help_text="List of speakers")
    partners = models.JSONField(default=list, blank=True, help_text="List of partner organizations")
    capacity = models.PositiveIntegerField(null=True, blank=True, help_text="Maximum number of participants")
    status = models.CharField(
        max_length=20,
        choices=EVENT_STATUS_CHOICES,
        default="upcoming",
        help_text="Current status of the event"
    )
    registration_required = models.BooleanField(default=True, help_text="Is registration required to attend?")
    registration_link = models.URLField(null=True, blank=True, help_text="Optional link for registration")


    council_members = models.ManyToManyField(
        "CouncilMembers.Council",
        through="CouncilEventParticipation",
        related_name="events"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-time"]
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return f"{self.title} ({self.time.strftime('%Y-%m-%d %H:%M')}) - {self.status}"


class CouncilEventParticipation(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="council_participations"
    )
    council_member = models.ForeignKey(
        "CouncilMembers.Council",
        on_delete=models.CASCADE,
        related_name="event_participations"
    )
    role_in_event = models.CharField(
        max_length=200,
        help_text="Role assigned to this council member in the event"
    )
    attended = models.BooleanField(
        default=False,
        help_text="Did the council member attend this event?"
    )

    class Meta:
        unique_together = ("event", "council_member")
        verbose_name = "Council Event Participation"
        verbose_name_plural = "Council Event Participations"

    def __str__(self):
        return f"{self.council_member} in {self.event} as {self.role_in_event}"
