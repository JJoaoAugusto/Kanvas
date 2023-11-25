from accounts.models import Account
from courses.models import Course
from .models import StudentCourse
from rest_framework import serializers


class StudentCourseSerializer(serializers.ModelSerializer):
    student_username = serializers.CharField(
        source="student.username",
        read_only=True
    )
    student_id = serializers.CharField(
        source="student.id",
        read_only=True
    )
    student_email = serializers.CharField(source="student.email")

    class Meta:
        model = StudentCourse
        fields = ["id", "student_username",
                  "student_email", "status", "student_id"]


class StudentCourseRegisterSerializer(serializers.ModelSerializer):
    students_courses = StudentCourseSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'students_courses']
        degth = 1
        extra_kwargs = {
            'name': {'read_only': True}
        }

    def update(self, instance, validated_data):
        found_students = []
        dont_students = []

        for student_course in validated_data['students_courses']:
            student = student_course['student']

            account = Account.objects.filter(email=student['email']).first()
            if not account:
                dont_students.append(student["email"])
            else:
                found_students.append(account)

        if dont_students:
            raise serializers.ValidationError({
                'detail': f'No active accounts was found: {", ".join(dont_students)}.'
            })

        if not self.partial:
            instance.students.add(*found_students)
            return instance

        return super().update(instance, validated_data)
