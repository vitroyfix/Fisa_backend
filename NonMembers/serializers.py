from rest_framework import serializers
from .models import NonMember

class NonMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonMember
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "institution",
            "events",
            "status",
            "registration_date",
            "attended_date",
            "feedback",
            "certificate_issued",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at", "registration_date", "attended_date"]
