from django.shortcuts import render ,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm,SMERegistrationForm
from django.contrib.auth import get_user,logout
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from coarse.models import Coarse
from coarse_content.models import CoarseContent
from coarse_enrollment.models import CoarseEnrollment
from bank.models import LoanService, InvestmentService
from django.contrib.auth import login
from app.settings import MEDIA_URL
from home.models import SiteDetails


@login_required(login_url='/learn/login')
def index(request):
    try:
        user = request.user
        user_enrollments = CoarseEnrollment.objects.filter(user=user)  # Assuming the relationship is updated in the model
        coarses = Coarse.objects.all()
    except CoarseEnrollment.DoesNotExist:
        return redirect('logout')
    site_details = SiteDetails.objects.all().first()
    context = {
        'user': user,
        'user_enrollments': user_enrollments,
        'coarses': coarses,
        'path': MEDIA_URL,
        'site_details': site_details
    }
    return render(request, 'home.html', context)

class UserLoginView(LoginView):
  template_name = 'login.html'
  form_class = LoginForm
  
  def get_success_url(self) -> str:
      return reverse_lazy('learn')

class UserRegistration(CreateView):
   template_name = 'register.html'
   form_class = RegistrationForm
   success_url = reverse_lazy('register_sme') 
   
   def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        print("******************")
        print(user)
        login(self.request, user)
        return response


@login_required(login_url='/learn/login')
def register_sme(request):
    if request.method == 'POST':
        form = SMERegistrationForm(request.POST)
        if form.is_valid():
            sme_registration = form.save(commit=False)
            sme_registration.user = request.user
            sme_registration.save()
            return redirect('learn')  # Redirect to a new URL
    else:
        form = SMERegistrationForm()
    return render(request, 'register_sme.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('learn')

def enroll_start(request):
    user = request.user
    coarse_id = request.GET.get('coarse', '')
    coarse = get_object_or_404(Coarse, id=coarse_id)
    user_enrollment, created = CoarseEnrollment.objects.get_or_create(
        user=user,  # Assuming relationship in CoarseEnrollment is updated
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
    user_enrollment = get_object_or_404(CoarseEnrollment, id=user_enrollment_id, user__user=request.user)
    
    coarse_contents = CoarseContent.objects.filter(coarse=user_enrollment.coarse)

    context = {
        'user_enrollment': user_enrollment,
        'coarse_contents': coarse_contents
    }

    return render(request, 'enroll.html', context)

@login_required(login_url='/learn/login')
def learning_resources(request):
    user = get_user(request)
    
    content_id  = request.GET.get('id', default='')
    coarse_content = CoarseContent.objects.get(id=content_id)

    context = {
         'coarse_content': coarse_content
     }

    return render(request, 'resources.html',context)

@login_required(login_url='/learn/login')
def my_coarses(request):
    user = request.user
    user_enrollments = CoarseEnrollment.objects.filter(user=user)  # Assuming relationship in CoarseEnrollment is updated
    coarses = Coarse.objects.all()
    context = {
        'user': user,
        'user_enrollments': user_enrollments,
        'coarses': coarses
    }
    return render(request, 'my_coarse.html', context)

@login_required(login_url='/learn/login')
def finServicesCategory(request):
    context = {}
    return render(request, 'fin_services_categories.html',context)

@login_required(login_url='/learn/login')
def learning_resources_details(request):
    user = get_user(request)
    bank_id  = request.GET.get('id', default='')
    bank = CoarseContent.objects.get(id=bank_id)

    context = {
         'bank': bank
     }

    return render(request, 'learning_resources_details.html',context)
