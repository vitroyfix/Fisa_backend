from rest_framework import viewsets, renderers, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import redirect
from .models import Media, PersonalMedia
from .serializers import MediaSerializer, PersonalMediaSerializer
from Student.models import Student


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all().order_by("-created_at")
    serializer_class = MediaSerializer
    renderer_classes = [renderers.JSONRenderer, renderers.TemplateHTMLRenderer]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    template_name = "media_list.html"

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if request.accepted_renderer.format == "html":
            return Response({"media_list": queryset}, template_name=self.template_name)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save()


class PersonalMediaViewSet(viewsets.ModelViewSet):
    queryset = PersonalMedia.objects.all().order_by("-created_at")
    serializer_class = PersonalMediaSerializer
    renderer_classes = [renderers.JSONRenderer, renderers.TemplateHTMLRenderer]
    permission_classes = [permissions.AllowAny]  # Change to IsAuthenticated if needed
    template_name = "profile.html"

    def perform_create(self, serializer):
        """Save media associated with the selected student."""
        serializer.save()

    def list(self, request, *args, **kwargs):
        student_id = request.GET.get("student")
        queryset = self.get_queryset()

        if student_id and student_id != "None":
            queryset = queryset.filter(student__id=student_id)

        if request.accepted_renderer.format == "html":
            students = Student.objects.all().order_by(
                "admissions__first_name", "admissions__last_name"
            )
            return Response(
                {
                    "personal_media_list": queryset,
                    "students": students,
                    "selected_student": student_id if student_id != "None" else "",
                },
                template_name=self.template_name,
            )

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """Handle uploads with a required student selection."""
        serializer = self.get_serializer(data=request.data, context={"request": request})

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        student = serializer.validated_data.get("student", None)
        if not student:
            return Response(
                {"student": "You must select a student for this upload."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        self.perform_create(serializer)

        if request.accepted_renderer.format == "html":
            return redirect(f"/api/media/personalmedia/?student={student.id}")

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        """Delete a PersonalMedia object using detail URL (/id/)"""
        return super().destroy(request, *args, **kwargs)

    
    @action(detail=False, methods=['delete'])
    def bulk_delete(self, request):
     
        media_id = request.data.get("id")
        if not media_id:
            return Response(
                {"detail": "You must provide 'id' to delete."},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            media = PersonalMedia.objects.get(id=media_id)
        except PersonalMedia.DoesNotExist:
            return Response(
                {"detail": f"PersonalMedia with id {media_id} does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        media.delete()
        return Response(
            {"detail": f"Deleted PersonalMedia with id {media_id}."},
            status=status.HTTP_200_OK
        )
