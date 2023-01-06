from django.forms import ModelForm
from django import forms
from .models import Student, Attendance

class UpdateStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class Attendance(ModelForm):

    class Meta:
        model = Attendance
        fields = '__all__'

