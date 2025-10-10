from rest_framework import serializers
from .models import NonMember
from Events.models import Event  # assuming you have an Event model


# Nested Event serializer (for read-only display)
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'date', 'location']  # include your actual Event fields


# NonMember serializer
class NonMemberSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True, read_only=True)

    class Meta:
        model = NonMember
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'institution',
            'status',
            'registration_date',
            'attended_date',
            'feedback',
            'certificate_issued',
            'events',
            'created_at',
            'updated_at',
        ]
