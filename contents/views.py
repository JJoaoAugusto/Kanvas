from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from .models import Content
from .serializers import ContentSerializer
from .permissions import IsAdmin, IsAdminOrStudent
from courses.models import Course


class ContentView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmin]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = 'course_id'

    def perform_create(self, serializer):
        found_course = get_object_or_404(
            Course, pk=self.kwargs.get('course_id'))
        return serializer.save(course=found_course)


class ContentDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrStudent]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = 'course_id'

    def get_object(self):
        try:
            Course.objects.get(id=self.kwargs['course_id'])
            content = Content.objects.get(id=self.kwargs['content_id'])

        except Course.DoesNotExist:
            raise NotFound({'detail': 'course not found.'})
        except Content.DoesNotExist:
            raise NotFound({'detail': 'content not found.'})

        self.check_object_permissions(self.request, content)
        return content
