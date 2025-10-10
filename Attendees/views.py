from rest_framework import viewsets, renderers
from rest_framework.response import Response
from .models import Attend
from .serializers import AttendSerializer

class AttendViewSet(viewsets.ModelViewSet):
    queryset = Attend.objects.all()
    serializer_class = AttendSerializer
    renderer_classes = [renderers.JSONRenderer, renderers.TemplateHTMLRenderer]
    template_name = "attendances.html"

    def get_queryset(self):
        return Attend.objects.select_related('student', 'event').all()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            return Response({'attend_list': self.get_queryset()})
        return response
