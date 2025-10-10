from rest_framework import serializers
from .models import Council

class CouncilSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(
        source='student.admissions.first_name', read_only=True
    )
    student_last_name = serializers.CharField(
        source='student.admissions.last_name', read_only=True
    )

    class Meta:
        model = Council
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
