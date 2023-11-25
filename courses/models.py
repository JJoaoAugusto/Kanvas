from uuid import uuid4
from django.db import models


class CourseStatus(models.TextChoices):
    NOT_STARTED = "not started"
    IN_PROGRESS = "in progress"
    FINISHED = "finished"


class Course(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=11,
        choices=CourseStatus.choices,
        default=CourseStatus.NOT_STARTED
    )
    start_date = models.DateField()
    end_date = models.DateField()

    instructor = models.ForeignKey(
        "accounts.Account",
        on_delete=models.PROTECT,
        related_name="courses",
        null=True,
    )

    students = models.ManyToManyField(
        'accounts.Account',
        related_name='my_courses',
        through='students_courses.StudentCourse'
    )
