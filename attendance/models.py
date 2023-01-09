from django.db import models

# Create your models here.


class Student(models.Model):
    matric_no   = models.CharField(max_length=100, blank=True, null=True)
    name        = models.CharField(max_length=400, blank=True, null=True)
    gender      = models.CharField(max_length=100, blank=True, null=True)
    email       = models.EmailField(max_length=254)
    session     = models.CharField(max_length=100, blank=True, null=True)
    level       = models.CharField(max_length=100, blank=True, null=True)
    department  = models.CharField(max_length=250, blank=True, null=True)
    


    def __str__(self):
        return f"{self.matric_no}"



class StudentAttendances(models.Model):
    SEMESTER = (
        ('1st', '1st'),
        ('2nd', '2nd')
        
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=False)
    semester    = models.CharField(max_length=100, blank=True, null=True, choices=SEMESTER)
    present = models.BooleanField(default=False)
    absent = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    




    
    
class Overall(models.Model):
    data = models.ForeignKey(StudentAttendances, on_delete=models.CASCADE)
    percentage = models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return self.data.student.matric_no + '  ' + self.percentage
    