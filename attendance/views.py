from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Student, StudentAttendances
from .forms import UpdateStudentForm,Attendance
from .filter import AttendanceFilter
from django.db.models import Count

# Create your views here.
def home(request):
    return render(request, "home.html")

def student_data(request):
    search_query = request.GET.get('search','')

    if search_query:
        stud_data = Student.objects.filter(Q(matric_no__icontains=search_query)| Q(name__icontains=search_query) | Q(level__icontains=search_query) | Q(department__icontains=search_query))
    else:
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
        session = request.POST['Session']

        stundent = Student.objects.create(matric_no=matric_no, name=name, gender=gender, email=email, level=level, department=department, session=session)
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
    if request.method == 'POST':
        form = Attendance(request.POST)
        if form.is_valid():
            form.save()
            return redirect('do-attendance')
    else:
        form = Attendance()

    student_attendance = StudentAttendances.objects.all()

    my_filter = AttendanceFilter(request.GET, queryset=student_attendance)
    student_attendance = my_filter.qs

    
    context = {'form':form, 'student_attendance':student_attendance, 'my_filter':my_filter}
    return render(request, 'attendance_record.html', context)



def dashboard(request):
    students = StudentAttendances.objects.filter(present=True).annotate(num_appearance=Count('present'))
    
    
    
    
    # for student in students:
    #     print = student.student.name,student.num_appearance 
    #     return print
    
    student = Student.objects.all() 
    student_total = len(student)
    
    
    
    
    context = {'print':students, 'student_total':student_total}
    return render(request, 'dashboard.html', context)

