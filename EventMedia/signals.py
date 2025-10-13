from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from Student.models import Student
from .models import PersonalMedia

User = get_user_model()


@receiver(post_save, sender=User)
def create_student_profile_image(sender, instance, created, **kwargs):
    if not created:
        return 
    try:
        student = getattr(instance, "student", None) or Student.objects.get(admissions__email=instance.email)

        if not PersonalMedia.objects.filter(student=student).exists():
            PersonalMedia.objects.create(student=student)
            print(f" Created empty profile image record for {student.full_name}")

    except Student.DoesNotExist:
        print(f" No Student found for user {instance.username}, skipping profile image creation.")
        return


@receiver(post_save, sender=PersonalMedia)
def update_student_profile_name(sender, instance, created, **kwargs):
   
    if created:
        print(f"Profile image record created for {instance.student.full_name}")
    else:
        print(f"Profile image updated for {instance.student.full_name}")
