from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Grade, Student, Subject


class EmployeeSignupForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class EmployeeLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "age", "email", "image", "password"]


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["name", "code", "description"]


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ["student", "subject", "score"]
