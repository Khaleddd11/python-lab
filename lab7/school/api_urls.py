from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api_views import (
    create_grade,
    create_subject,
    get_all_grades,
    get_all_subjects,
    GradeDetailView,
    GradeViewSet,
    StudentDetailView,
    StudentViewSet,
    SubjectCBV,
    SubjectViewSet,
    login,
    logout,
    register,
    students_fbv,
)

router = DefaultRouter()
router.register(r"students-v2", StudentViewSet, basename="students-v2")
router.register(r"subjects-v2", SubjectViewSet, basename="subjects-v2")
router.register(r"grades-viewset", GradeViewSet, basename="grades-viewset")

urlpatterns = [
    path("register/", register, name="api-register"),
    path("login/", login, name="api-login"),
    path("logout/", logout, name="api-logout"),
    path("students-fbv/", students_fbv, name="students-fbv"),
    path("students-cbv/<int:pk>/", StudentDetailView.as_view(), name="students-cbv"),
    path("subjects/create/", create_subject, name="subjects-create"),
    path("subjects/all/", get_all_subjects, name="subjects-all"),
    path("subjects-cbv/<int:pk>/", SubjectCBV.as_view(), name="subjects-cbv"),
    path("grades/create/", create_grade, name="grades-create"),
    path("grades/all/", get_all_grades, name="grades-all"),
    path("grades-cbv/<int:pk>/", GradeDetailView.as_view(), name="grades-cbv"),
    path("", include(router.urls)),
]
