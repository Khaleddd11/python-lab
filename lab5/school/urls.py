from django.urls import path
from school.views import home, students, student_delete, contact_us

urlpatterns = [
    path("", home, name="home"),
    path("students/", students, name="students"),
    path("students_delete/<int:id>/", student_delete, name="student_delete"),
    path("contact/", contact_us, name="contact_us"),
]