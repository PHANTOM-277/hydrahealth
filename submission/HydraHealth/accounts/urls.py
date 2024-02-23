from django.urls import path, include
from . import views

app_name='accounts'
urlpatterns = [
    path('',views.login_as, name='login_as'),
    path('which_student',views.which_student, name='which_studnet'),
    path('teacher_login',views.teacher_login, name='teacher_login'),
    path('login_student',views.student_login,name='student_login'),
    path('register',views.register,name='register'),
]