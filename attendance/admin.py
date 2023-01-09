from django.contrib import admin
from .models import Student, StudentAttendances, Overall

# Register your models here.
admin.site.register(Student)
admin.site.register(StudentAttendances)
admin.site.register(Overall)