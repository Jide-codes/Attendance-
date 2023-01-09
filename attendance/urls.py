from django.urls import path
from . import views
urlpatterns = [

    path('', views.home, name='home' ),
    path('student-data/', views.student_data, name='student-data' ),
    path('student-form/', views.add_student_info, name='student-form' ),
    path('update-student-info/<str:pk>/', views.update_student_info, name='update-info' ),
    path('delete-student-info/<str:pk>/', views.delete_student_info, name='delete-info' ),
    path('do-attendance/', views.do_attendance, name='do-attendance'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('overall_report/', views.overall_report, name='overall-report'),

    path('successful/', views.successful, name='successful')
]
