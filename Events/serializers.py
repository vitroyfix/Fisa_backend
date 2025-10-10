from rest_framework import serializers
from .models import Event, CouncilEventParticipation


class CouncilEventParticipationSerializer(serializers.ModelSerializer):
    council_member_name = serializers.CharField(
        source='council_member.name', read_only=True
    )

    class Meta:
        model = CouncilEventParticipation
        fields = [
            'id',
            'event',
            'council_member',
            'council_member_name',
            'role_in_event',
            'attended',
        ]


class EventSerializer(serializers.ModelSerializer):
    council_participations = CouncilEventParticipationSerializer(
        many=True, read_only=True
    )

    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'description',
            'location',
            'time',
            'end_time',
            'speakers',
            'partners',
            'capacity',
            'status',
            'registration_required',
            'registration_link',
            'council_participations',
            'created_at',
            'updated_at',
        ]
