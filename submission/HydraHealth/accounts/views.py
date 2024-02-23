from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def login_as(request):
    return render(request, 'accounts/login.html')

def which_student(request):
    return render(request, 'accounts/login_which_student.html')

def teacher_login(request):
    return render(request, 'accounts/login_teacher.html')

def student_login(request):
    if request.method == 'POST':
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                # Attempt to authenticate the user
                user = authenticate(request, username=email, password=password)
                if user is not None:
                    # If authentication succeeds, log in the user
                    login(request, user)
                    # Redirect to a success page (e.g., dashboard)
                    return redirect('grades:dashboard')
    return render(request, 'accounts/login_student.html')

def register(request):
    return render(request, 'accounts/register.html')

