from django.urls import path
from .views import CourseView, CourseDetailView

urlpatterns = [
    path('courses/', CourseView.as_view()),
    path('courses/<uuid:course_id>/', CourseDetailView.as_view())
]
