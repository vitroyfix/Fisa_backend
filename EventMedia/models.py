# models.py
from django.db import models

class Media(models.Model):
    CATEGORY_CHOICES = [
        ("event", "Event"),
        ("lecture", "Lecture"),
        ("announcement", "Announcement"),
    ]

    MEDIA_TYPE_CHOICES = [
        ("video", "Video"),
        ("image", "Image"),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="event")
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    media_file = models.FileField(upload_to="uploads/media/")
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)      

    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Media Files"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.category} - {self.title} ({self.media_type})"
