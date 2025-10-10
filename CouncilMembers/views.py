from rest_framework import viewsets, renderers
from rest_framework.response import Response
from .models import Council
from .serializers import CouncilSerializer

class CouncilViewSet(viewsets.ModelViewSet):
    queryset = Council.objects.all()
    serializer_class = CouncilSerializer
    renderer_classes = [renderers.JSONRenderer, renderers.TemplateHTMLRenderer]
    template_name = "council_members.html"

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if request.accepted_renderer.format == 'html':
            
            return Response({'council_members': queryset})
        else:
            
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
