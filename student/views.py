from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AuthenticationForm, RegisterForm
from django.contrib.auth import get_user,authenticate,login,logout,get_user_model
from .models import Student
from coarse.models import Coarse
from coarse_content.models import CoarseContent
from coarse_enrollment.models import CoarseEnrollment
from bank.models import Bank


@login_required(login_url='/learn/login')
def index(request):
    try:
        user = get_user(request)
        student = Student.objects.get(user=user)
        user_enrollments = CoarseEnrollment.objects.filter(student=student)
        print(user_enrollments)
        coarses = Coarse.objects.all()
    except (Student.DoesNotExist):

        return redirect('logout')

    context = {
         'user': user,
         'user_enrollments': user_enrollments,
         'coarses': coarses
     }
    return render(request, 'home.html',context)

def signin(request):
    form = AuthenticationForm()
    user = get_user(request)
    username = user.get_username()

    context = {
        'form': form,
        'user': user,
        'username': username,
        'site_url': 'http://127.0.0.1:8000/',

    }

    if request.method == 'POST':
        messages.success(request, f'Please wait....')
        username =  request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:

            messages.success(request, f'you are now logged in')
            login(request,user)
               
            return redirect('learn')
        else:
            messages.error(request, f'Log-in attempt failed!!')
    
    return render(request, 'login.html',context)

def register(request):

    form = RegisterForm(request.POST)
    user = get_user(request)
    username = user.get_username()


    if request.method == 'POST':
        
        if form.is_valid():
            form.save(commit=True)
            return redirect('learn')
    context = {
        'form': form,
        'user': user,
        'username': username,
        'site_url': 'http://127.0.0.1:8000/',

    }
    return render(request, 'register.html', context)

def signout(request):
    logout(request)
    return redirect('learn')

@login_required(login_url='/learn/login')
def enroll_start(request):
    user = get_user(request)
    student = Student.objects.get(user=user)
    coarse_id = request.GET.get('coarse', default='')
    coarse = Coarse.objects.get(id=int(coarse_id))
    user_enrollment = CoarseEnrollment.objects.create(
        student=student,
        coarse=coarse,
        progress=0.0
    )
    coarse_content = CoarseContent.objects.filter(coarse=coarse)
    coarse_content = CoarseContent.objects.filter(coarse=user_enrollment.coarse)

    context = {
         'user': user,
         'user_enrollment': user_enrollment,
         'coarse': coarse,
         'coarse_content': coarse_content
     }
    

    return render(request, 'enroll.html',context)

@login_required(login_url='/learn/login')
def learn_start(request):
    user = get_user(request)
    student = Student.objects.get(user=user)
    user_enrollment_id  = request.GET.get('id', default='')
    user_enrollment = CoarseEnrollment.objects.get(id=int(user_enrollment_id))
    coarse_contents = CoarseContent.objects.filter(coarse=user_enrollment.coarse)

    context = {
         'user': user,
         'user_enrollment': user_enrollment,
         'coarse': user_enrollment.coarse,
         'coarse_contents': coarse_contents
     }

    return render(request, 'enroll.html',context)

@login_required(login_url='/learn/login')
def learning_resources(request):
    user = get_user(request)
    student = Student.objects.get(user=user)
    content_id  = request.GET.get('id', default='')
    coarse_content = CoarseContent.objects.get(id=content_id)

    context = {
         'coarse_content': coarse_content
     }

    return render(request, 'resources.html',context)

@login_required(login_url='/learn/login')
def my_coarses(request):
    try:
        user = get_user(request)
        student = Student.objects.get(user=user)
        user_enrollments = CoarseEnrollment.objects.filter(student=student)
        coarses = Coarse.objects.all()
    except (Student.DoesNotExist):

        return redirect('logout')

    context = {
         'user': user,
         'user_enrollments': user_enrollments,
         'coarses': coarses
     }
    return render(request, 'my_coarse.html',context)

@login_required(login_url='/learn/login')
def resources(request):
    try:
        user = get_user(request)
        student = Student.objects.get(user=user)
        user_enrollments = CoarseEnrollment.objects.filter(student=student)
        banks = Bank.objects.all()
    except (Student.DoesNotExist):
        return redirect('logout')
    context = {
         'user': user,
         'user_enrollments': user_enrollments,
         'banks': banks
     }
    return render(request, 'learning_resources.html',context)

@login_required(login_url='/learn/login')
def learning_resources_details(request):
    user = get_user(request)
    student = Student.objects.get(user=user)
    bank_id  = request.GET.get('id', default='')
    bank = CoarseContent.objects.get(id=bank_id)

    context = {
         'bank': bank
     }

    return render(request, 'learning_resources_details.html',context)
