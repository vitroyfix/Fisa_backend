from rest_framework import serializers
from .models import Student
from Admissions.models import Admission


class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "email",
            "phone_number",
            "course",
            "year_of_study",
            "admission_date",
            "gender",
            "date_of_birth",
            "status",
        ]

class StudentSerializer(serializers.ModelSerializer):
    admissions = AdmissionSerializer(read_only=True)

    class Meta:
        model = Student
        fields = [
            "id",
            "admissions",
            "created_at",
            "updated_at",
        ]
