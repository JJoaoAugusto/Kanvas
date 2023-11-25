from uuid import uuid4
from django.db import models


class StudentCourseStatus(models.TextChoices):
    PENDING = 'pending'
    ACCEPTED = 'accepted'


class StudentCourse(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    status = models.CharField(
        max_length=20,
        choices=StudentCourseStatus.choices,
        default=StudentCourseStatus.PENDING
    )

    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        related_name='students_courses'
    )

    student = models.ForeignKey(
        'accounts.Account',
        on_delete=models.CASCADE,
        related_name='students_courses'
    )
