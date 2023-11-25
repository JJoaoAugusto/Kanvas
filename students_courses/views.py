from rest_framework.generics import RetrieveUpdateAPIView
from courses.models import Course
from .serializers import StudentCourseRegisterSerializer


class StudentCourseView(RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = StudentCourseRegisterSerializer
    lookup_url_kwarg = "course_id"
