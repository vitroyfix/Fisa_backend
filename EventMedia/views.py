from rest_framework import viewsets, renderers
from rest_framework.response import Response
from .models import Media
from .serializers import MediaSerializer 

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    renderer_classes = [renderers.JSONRenderer, renderers.TemplateHTMLRenderer]
    template_name = "media_list.html"  
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            
            return Response({'media_list': self.get_queryset()})
        return response
