from django.db import models


class Media(models.Model):
    CATEGORY_CHOICES = [
        ("event", "Event"),
        ("lecture", "Lecture"),
        ("announcement", "Announcement"),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="event")
    media_type = models.CharField(max_length=10, choices=[("video", "Video"), ("image", "Image")])
    media_file = models.FileField(upload_to="uploads/media/")

    def __str__(self):
        return f"{self.category} - {self.title} ({self.media_type})"
