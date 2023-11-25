from rest_framework import serializers

from .models import Course
from contents.serializers import ContentSerializer
from students_courses.serializers import StudentCourseSerializer
from accounts.serializers import AccountSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'status', 'start_date', 'end_date',
                  'instructor', 'contents', 'students_courses']
        extra_kwargs = {
            'contents': {'read_only': True},
            'students_courses': {'read_only': True}
        }


class CourseDetailSerializer(serializers.ModelSerializer):
    instructor = AccountSerializer(read_only=True, many=True)
    students_courses = StudentCourseSerializer(read_only=True, many=True)
    contents = ContentSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'status', 'start_date', 'end_date',
                  'instructor', 'contents', 'students_courses']
