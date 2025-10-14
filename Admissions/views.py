from rest_framework import viewsets, status, renderers
from rest_framework.response import Response
from .models import Admission
from .serializers import AdmissionSerializer

class AdmissionViewSet(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
    renderer_classes = [renderers.JSONRenderer, renderers.TemplateHTMLRenderer]
    template_name = "admissions.html"

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        if request.accepted_renderer.format == "html":
            return Response({"admissions": queryset}, template_name=self.template_name)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # Ensure new submissions have status "pending"
        data = request.data.copy()
        data['status'] = 'pending'

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            admission = serializer.save()

            if request.accepted_renderer.format == "html":
                context = {
                    "admissions": self.get_queryset(),
                    "message": "Student registered successfully. Waiting for admin approval.",
                }
                return Response(context, template_name=self.template_name)

            return Response(
                {
                    "message": "Student registered successfully. Waiting for admin approval.",
                    "student": self.get_serializer(admission).data,
                },
                status=status.HTTP_201_CREATED,
            )

        if request.accepted_renderer.format == "html":
            return Response(
                {"errors": serializer.errors, "admissions": self.get_queryset()},
                template_name=self.template_name,
            )

        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
