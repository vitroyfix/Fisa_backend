# serializers.py
from rest_framework import serializers
from .models import Media

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = [
            'id',
            'title',
            'category',
            'media_type',
            'media_file',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
