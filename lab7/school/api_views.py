from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Grade, Student, Subject
from .serializers import GradeSerializer, StudentSerializer, SubjectSerializer, UserSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")

    if not username or not password or not email:
        return Response({"error": "Username, password and email are required."}, status=400)
    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists."}, status=400)

    user = User.objects.create_user(username=username, password=password, email=email)
    token = Token.objects.create(user=user)
    return Response(
        {"msg": "User registered successfully.", "token": token.key, "user": UserSerializer(user).data},
        status=201,
    )


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"error": "Username and password are required."}, status=400)

    user = authenticate(request, username=username, password=password)
    if user is not None:
        Token.objects.filter(user=user).delete() # delete old token
        token = Token.objects.create(user=user) #create new token
        return Response(
            {"msg": "Login successful.", "token": token.key, "user": UserSerializer(user).data},
            status=200,
        )
    return Response({"error": "Invalid credentials."}, status=401)


@api_view(["POST"])
@permission_classes([AllowAny])
def logout(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"error": "Username and password are required."}, status=400)

    user = authenticate(request, username=username, password=password)
    if user is not None:
        Token.objects.filter(user=user).delete()
        return Response({"msg": "Logout successful."}, status=200)
    return Response({"error": "Invalid credentials."}, status=401)


@api_view(["GET", "POST"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def students_fbv(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response({"msg": "Students retrieved successfully.", "data": serializer.data}, status=200)

    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"msg": "Student created successfully.", "data": serializer.data}, status=201)
    return Response({"error": "Invalid data.", "details": serializer.errors}, status=400)


@api_view(["GET"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_all_subjects(request):
    subjects = Subject.objects.all()
    serializer = SubjectSerializer(subjects, many=True)
    return Response({"msg": "Subjects retrieved successfully.", "data": serializer.data}, status=200)


@api_view(["POST"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def create_subject(request):
    serializer = SubjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"msg": "Subject created successfully.", "data": serializer.data}, status=201)
    return Response({"error": "Invalid data.", "details": serializer.errors}, status=400)


@api_view(["GET"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_all_grades(request):
    grades = Grade.objects.select_related("student", "subject").all()
    serializer = GradeSerializer(grades, many=True)
    return Response({"msg": "Grades retrieved successfully.", "data": serializer.data}, status=200)


@api_view(["POST"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def create_grade(request):
    serializer = GradeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"msg": "Grade created successfully.", "data": serializer.data}, status=201)
    return Response({"error": "Invalid data.", "details": serializer.errors}, status=400)


class SubjectCBV(APIView): #inherit from apiview
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            subject = Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            return Response({"error": "Subject not found."}, status=404)
        serializer = SubjectSerializer(subject)
        return Response({"msg": "Subject retrieved successfully.", "data": serializer.data}, status=200)

    def put(self, request, pk):
        try:
            subject = Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            return Response({"error": "Subject not found."}, status=404)
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Subject updated successfully.", "data": serializer.data}, status=200)
        return Response({"error": "Invalid data.", "details": serializer.errors}, status=400)

    def delete(self, request, pk):
        try:
            subject = Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            return Response({"error": "Subject not found."}, status=404)
        subject.delete()
        return Response({"msg": "Subject deleted successfully."}, status=200)


class StudentDetailView(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({"error": "Student not found."}, status=404)
        serializer = StudentSerializer(student)
        return Response({"msg": "Student retrieved successfully.", "data": serializer.data}, status=200)

    def put(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({"error": "Student not found."}, status=404)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Student updated successfully.", "data": serializer.data}, status=200)
        return Response({"error": "Invalid data.", "details": serializer.errors}, status=400)

    def delete(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({"error": "Student not found."}, status=404)
        student.delete()
        return Response({"msg": "Student deleted successfully."}, status=200)


class GradeDetailView(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            grade = Grade.objects.select_related("student", "subject").get(pk=pk)
        except Grade.DoesNotExist:
            return Response({"error": "Grade not found."}, status=404)
        serializer = GradeSerializer(grade)
        return Response({"msg": "Grade retrieved successfully.", "data": serializer.data}, status=200)

    def put(self, request, pk):
        try:
            grade = Grade.objects.get(pk=pk)
        except Grade.DoesNotExist:
            return Response({"error": "Grade not found."}, status=404)
        serializer = GradeSerializer(grade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Grade updated successfully.", "data": serializer.data}, status=200)
        return Response({"error": "Invalid data.", "details": serializer.errors}, status=400)

    def delete(self, request, pk):
        try:
            grade = Grade.objects.get(pk=pk)
        except Grade.DoesNotExist:
            return Response({"error": "Grade not found."}, status=404)
        grade.delete()
        return Response({"msg": "Grade deleted successfully."}, status=200)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["age", "email"]
    search_fields = ["name", "email"]
    ordering_fields = ["name", "age"]
    ordering = ["name"]


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["name", "code"]
    search_fields = ["name", "code", "description"]
    ordering_fields = ["name", "code"]
    ordering = ["name"]


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.select_related("student", "subject").all()
    serializer_class = GradeSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["student", "subject", "score"]
    search_fields = ["student__name", "subject__name"]
    ordering_fields = ["score", "student__name", "subject__name"]
    ordering = ["-score"]
