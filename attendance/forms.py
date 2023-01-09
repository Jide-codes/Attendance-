from django.forms import ModelForm
from django import forms
from .models import Student, StudentAttendances

class UpdateStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'



class Attendance(ModelForm):

    class Meta:
        model = StudentAttendances
        fields = ['student', 'semester', 'present', 'absent']
        widgets={
            'student'
            'semester': forms.TextInput(attrs={'class': 'form-control'}),
            'present': forms.CheckboxInput(),
            'absent': forms.CheckboxInput(),
        }