from rest_framework import viewsets, renderers
from rest_framework.response import Response
from .models import Event, CouncilEventParticipation
from .serializers import EventSerializer, CouncilEventParticipationSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    renderer_classes = [renderers.JSONRenderer, renderers.TemplateHTMLRenderer]
    template_name = "events.html"

    def get_queryset(self):
        return Event.objects.prefetch_related(
            "council_participations__council_member__student"
        ).all()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if request.accepted_renderer.format == "html":
            return Response({"events": self.get_queryset()})
        return response


class CouncilEventParticipationViewSet(viewsets.ModelViewSet):
    queryset = CouncilEventParticipation.objects.select_related(
        "event", "council_member__student"
    ).all()
    serializer_class = CouncilEventParticipationSerializer
    renderer_classes = [renderers.JSONRenderer, renderers.TemplateHTMLRenderer]
    template_name = "council_participations.html"

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if request.accepted_renderer.format == "html":
            return Response({"participations": self.get_queryset()})
        return response
