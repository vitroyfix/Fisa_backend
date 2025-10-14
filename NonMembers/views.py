from rest_framework import viewsets, status, renderers
from rest_framework.response import Response
from .models import NonMember
from .serializers import NonMemberSerializer

class NonMemberViewSet(viewsets.ModelViewSet):
    queryset = NonMember.objects.all()
    serializer_class = NonMemberSerializer
    renderer_classes = [renderers.JSONRenderer, renderers.TemplateHTMLRenderer]
    template_name = "nonmembers.html" 

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        if request.accepted_renderer.format == "html":
            
            return Response({"non_members": queryset}, template_name=self.template_name)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['status'] = 'registered'

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            non_member = serializer.save()

            if request.accepted_renderer.format == "html":
                context = {
                    "non_members": self.get_queryset(),
                    "message": "Non-member registered successfully.",
                }
                return Response(context, template_name=self.template_name)

            return Response(
                {
                    "message": "Non-member registered successfully.",
                    "non_member": self.get_serializer(non_member).data,
                },
                status=status.HTTP_201_CREATED,
            )

        if request.accepted_renderer.format == "html":
            return Response(
                {"errors": serializer.errors, "non_members": self.get_queryset()},
                template_name=self.template_name,
            )

        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
