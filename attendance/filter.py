import django_filters
from .models import *

class AttendanceFilter(django_filters.FilterSet):
    class Meta:
        model = StudentAttendances
        fields = ['student',  'semester']