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



class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=False)
    semester    = models.CharField(max_length=100, blank=True, null=True)
    attendance = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    

    def what_to_return(self):
        if self.attendance:
            return 'Yes'
        else:
            return 'No'

    def __str__(self):
        if self.attendance:
            return 'present'
        else:
            return 'absent'
    
class Overall(models.Model):
    data = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    percentage = models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return self.data.student.matric_no + '  ' + self.percentage
    