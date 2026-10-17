from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("students/", views.student_list, name="student_list"),
    path("teachers/", views.teacher_list, name="teacher_list"),
    path("courses/", views.course_list, name="course_list"),
    path("enrollment/", views.enrollment, name="enrollment"),

    path("students/<str:student_id>/delete/", views.delete_student, name="delete_student"),
    path("teachers/<str:teacher_id>/delete/", views.delete_teacher, name="delete_teacher"),
    path("courses/<str:course_code>/delete/", views.delete_course, name="delete_course"),


]