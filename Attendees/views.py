from rest_framework import viewsets, renderers
from rest_framework.response import Response
from .models import Attend
from .serializers import AttendSerializer


class AttendViewSet(viewsets.ModelViewSet):
    queryset = Attend.objects.select_related('student', 'event').all()
    serializer_class = AttendSerializer
    renderer_classes = [renderers.JSONRenderer, renderers.TemplateHTMLRenderer]
    template_name = "attendances.html"

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if request.accepted_renderer.format == 'html':
            context = {'attend_list': queryset}
            return Response(context, template_name=self.template_name)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
