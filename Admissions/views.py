from rest_framework import viewsets, renderers
from rest_framework.response import Response
from .models import Admission
from .serializers import AdmissionSerializer

class AdmissionViewSet(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
    renderer_classes = [renderers.TemplateHTMLRenderer, renderers.JSONRenderer]
    template_name = 'admissions.html'

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
    
        return Response({'admissions': serializer.data}, template_name=self.template_name)
