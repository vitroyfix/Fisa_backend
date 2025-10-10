from rest_framework import serializers
from .models import Attend

class AttendSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(
        source='student.admissions.first_name', read_only=True
    )
    event_title = serializers.CharField(
        source='event.title', read_only=True
    )

    class Meta:
        model = Attend
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
