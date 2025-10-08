# Admissions/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Admission
from Student.models import Student

@receiver(post_save, sender=Admission)
def create_student_for_approved_admission(sender, instance, created, **kwargs):
    if instance.status == "approved" and not hasattr(instance, "student"):
        Student.objects.create(admissions=instance)
