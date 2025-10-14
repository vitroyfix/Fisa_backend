from rest_framework import serializers
from .models import Media, PersonalMedia
import hashlib


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

    def _file_hash(self, file):
        """Compute MD5 hash of uploaded file for duplicate detection"""
        hasher = hashlib.md5()
        for chunk in file.chunks():
            hasher.update(chunk)
        return hasher.hexdigest()

    def create(self, validated_data):
        student = validated_data.get("student")
        if not student:
            raise serializers.ValidationError({
                "student": "You must select a student for this upload."
            })

        new_image = validated_data.get("image")
        new_cover = validated_data.get("cover_image")

        # Check for duplicates among existing uploads
        existing_media = PersonalMedia.objects.filter(student=student)
        for media in existing_media:
            if new_image and media.image:
                if self._file_hash(new_image) == self._file_hash(media.image):
                    raise serializers.ValidationError({"image": "This profile image has already been uploaded."})
            if new_cover and media.cover_image:
                if self._file_hash(new_cover) == self._file_hash(media.cover_image):
                    raise serializers.ValidationError({"cover_image": "This cover image has already been uploaded."})

        # Create a new PersonalMedia record
        personal_media = PersonalMedia.objects.create(**validated_data)
        return personal_media
