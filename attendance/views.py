from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Attendance
from .forms import UpdateStudentForm,Attendance
# Create your views here.
def home(request):
    return render(request, "home.html")

def student_data(request):
    stud_data = Student.objects.all()
    context = {'datas':stud_data}
    return render(request, "student_data.html", context)

def add_student_info(request):
    if request.method == 'POST':
        matric_no = request.POST['MatricNo']
        name = request.POST['Student_name']
        gender = request.POST['Gender']
        email = request.POST['Email']
        level = request.POST['Level']
        department = request.POST['Department']
        semester = request.POST['Semester']
        session = request.POST['Session']

        stundent = Student.objects.create(matric_no=matric_no, name=name, gender=gender, email=email, level=level, department=department, semester=semester, session=session)
        stundent.save()
        print('saved!')
        return redirect('student-data')
        
    context = {}
    return render(request, "student_form.html", context)


def update_student_info(request, pk):

    student = Student.objects.get(id=pk)
    form = UpdateStudentForm(instance=student)
    if request.method == 'POST':
        form = UpdateStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student-data')
 

    context = {'form':form}
    return render(request, "update-form.html", context)


def delete_student_info(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('student-data')


# Here Comes The Logic
def successful(request):
    return render(request, 'succesful.html')


def do_attendance(request):

    context = {}
    return render(request, 'attendance_record.html', context)



def attendance_table(request):
    attendance = Attendance.objects.all()
    context = {'attendance':attendance}
    return render(request, 'attendance_table.html', context)

