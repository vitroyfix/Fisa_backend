from rest_framework import serializers
from .models import Media, PersonalMedia


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = [
            "id",
            "title",
            "category",
            "media_type",
            "media_file",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class PersonalMediaSerializer(serializers.ModelSerializer):
    student_full_name = serializers.CharField(source="student.full_name", read_only=True)
    image_url = serializers.SerializerMethodField()
    cover_image_url = serializers.SerializerMethodField()

    class Meta:
        model = PersonalMedia
        fields = [
            "id",
            "student",
            "student_full_name",
            "image",
            "image_url",
            "cover_image",
            "cover_image_url",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "student_full_name", "created_at", "updated_at"]

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image:
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None

    def get_cover_image_url(self, obj):
        request = self.context.get("request")
        if obj.cover_image:
            return request.build_absolute_uri(obj.cover_image.url) if request else obj.cover_image.url
        return None

    def create(self, validated_data):
       
        student = validated_data.get("student")

        if not student:
            raise serializers.ValidationError({
                "student": "You must select a student for this upload."
            })

        personal_media = PersonalMedia.objects.create(**validated_data)
        return personal_media

