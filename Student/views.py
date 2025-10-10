from rest_framework import viewsets, renderers
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().select_related('admissions')
    serializer_class = StudentSerializer
    renderer_classes = [renderers.JSONRenderer, renderers.TemplateHTMLRenderer]
    template_name = "students.html"

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
        
            return Response({'students': self.get_queryset()})
        return response
