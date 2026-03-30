from django.contrib import admin
from .models import Grade, Student, Subject

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Grade)
