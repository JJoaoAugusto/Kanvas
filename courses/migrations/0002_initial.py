# Generated by Django 4.2.6 on 2023-10-31 19:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students_courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_name='my_courses', through='students_courses.StudentCourse', to=settings.AUTH_USER_MODEL),
        ),
    ]
