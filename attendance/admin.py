from django.contrib import admin
from .models import Student, Attendance, Overall

# Register your models here.
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Overall)