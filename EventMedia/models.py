from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver


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


class PersonalMedia(models.Model):
    student = models.ForeignKey(
        "Student.Student",
        on_delete=models.CASCADE,
        related_name="personal_media",
        verbose_name="Student",
        null=True, 
        blank=True
    )
    image = models.ImageField(upload_to="uploads/profile_images/", null=True, blank=True)
    cover_image = models.ImageField(upload_to="uploads/cover_images/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Personal Media"
        verbose_name_plural = "Personal Media"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Media for {self.student.full_name if self.student else 'Unassigned'}"

    def clean(self):
        if not self.image and not self.cover_image:
            raise ValidationError("You must upload either a profile image or a cover image.")

        valid_extensions = [".jpg", ".jpeg", ".png", ".gif", ".webp"]
        for field in [self.image, self.cover_image]:
            if field and not any(field.name.lower().endswith(ext) for ext in valid_extensions):
                raise ValidationError("Only image files are allowed (JPG, PNG, GIF, or WEBP).")

    def save(self, *args, **kwargs):
        try:
            old_instance = PersonalMedia.objects.get(pk=self.pk)
            if old_instance.image and old_instance.image != self.image:
                old_instance.image.delete(save=False)
            if old_instance.cover_image and old_instance.cover_image != self.cover_image:
                old_instance.cover_image.delete(save=False)
        except PersonalMedia.DoesNotExist:
            pass
        super().save(*args, **kwargs)

    @property
    def image_url(self):
        return self.image.url if self.image else None

    @property
    def cover_image_url(self):
        return self.cover_image.url if self.cover_image else None


@receiver(post_save, sender="Student.Student")
def create_student_media(sender, instance, created, **kwargs):
    if created:
        PersonalMedia.objects.create(student=instance)
