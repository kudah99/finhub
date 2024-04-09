from django.shortcuts import render ,redirect, get_object_or_404
from django.contrib import messages
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import get_user,authenticate,login,logout,get_user_model
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from .models import Student
from django.views.generic import CreateView
from django.urls import reverse_lazy
from coarse.models import Coarse
from coarse_content.models import CoarseContent
from coarse_enrollment.models import CoarseEnrollment
from bank.models import Bank ,FinancialServiceCategory


@login_required(login_url='/learn/login')
def index(request):
    try:
        user = get_user(request)
        student = Student.objects.get(user=user)
        user_enrollments = CoarseEnrollment.objects.filter(student=student)
        print(user_enrollments)
        coarses = Coarse.objects.all()
    except (Student.DoesNotExist):
        if user is not None:
            if user.is_staff:
                logout(request)
            else:
                Student.objects.create(user=user)
                return redirect('learn')
        return redirect('logout')

    context = {
         'user': user,
         'user_enrollments': user_enrollments,
         'coarses': coarses
     }
    return render(request, 'home.html',context)

class UserLoginView(LoginView):
  template_name = 'login.html'
  form_class = LoginForm
  
  def get_success_url(self) -> str:
      return reverse_lazy('learn')

class UserRegistration(CreateView):
   template_name = 'register.html'
   form_class = RegistrationForm
   success_url = "/learn/"


def create_student(request):
    logout(request)
    return redirect('learn')

def signout(request):
    logout(request)
    return redirect('learn')

@login_required(login_url='/learn/login')
def enroll_start(request):
    user = request.user
    coarse_id = request.GET.get('coarse', '')
    coarse = get_object_or_404(Coarse, id=coarse_id)
    student = get_object_or_404(Student, user=user)
    
    user_enrollment, created = CoarseEnrollment.objects.get_or_create(
        student=student,
        coarse=coarse,
        defaults={'progress': 0.0}
    )
    
    coarse_content = CoarseContent.objects.filter(coarse=coarse)

    context = {
        'user_enrollment': user_enrollment,
        'coarse': coarse,
        'coarse_content': coarse_content
    }

    return render(request, 'enroll.html', context)

@login_required(login_url='/learn/login')
def learn_start(request):
    user_enrollment_id = request.GET.get('id', '')
    user_enrollment = get_object_or_404(CoarseEnrollment, id=user_enrollment_id, student__user=request.user)
    
    coarse_contents = CoarseContent.objects.filter(coarse=user_enrollment.coarse)

    context = {
        'user_enrollment': user_enrollment,
        'coarse_contents': coarse_contents
    }

    return render(request, 'enroll.html', context)

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
def finServicesCategory(request):
    categories = FinancialServiceCategory.objects.all()
    banks = []

    if request.method == 'POST':
        id = request.POST['id']
        category = FinancialServiceCategory.objects.get(id=int(id))
        banks = Bank.objects.filter(category=category)
        context = {
         'category': category,
         'banks': banks
         }

        return render(request, 'bank_list.html',context)

    context = {
         'categories': categories,
         'banks': banks
     }
    return render(request, 'fin_services_categories.html',context)

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
