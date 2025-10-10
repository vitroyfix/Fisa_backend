from rest_framework import viewsets, renderers
from rest_framework.response import Response
from .models import NonMember
from .serializers import NonMemberSerializer

class NonMemberViewSet(viewsets.ModelViewSet):
 
    queryset = NonMember.objects.prefetch_related('events').all()
    serializer_class = NonMemberSerializer
    renderer_classes = [renderers.JSONRenderer, renderers.TemplateHTMLRenderer]
    template_name = 'nonmembers.html'

    def list(self, request, *args, **kwargs):
        
        response = super().list(request, *args, **kwargs)

        if request.accepted_renderer.format == 'html':
            nonmembers = self.get_queryset()
            return Response({'nonmembers': nonmembers}, template_name=self.template_name)

        return response
