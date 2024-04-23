from django.shortcuts import render ,redirect, get_object_or_404
from django import template
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm,SMERegistrationForm
from django.contrib.auth import get_user,logout
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from coarse.models import Coarse
from coarse_content.models import CoarseContent
from coarse_enrollment.models import CoarseEnrollment
from financial_service.models import LoanService, InvestmentService
from django.views.generic import DetailView
from datetime import date
from django.db.models import Q
from django.contrib.auth import login
from app.settings import MEDIA_URL
from home.models import SiteDetails
from .models import  SMERegistration

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
   success_url = reverse_lazy('learn') 
   
   def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        if user.business_owner:
            # Redirect to SME registration if the user is a business owner
            self.success_url = reverse_lazy('register_sme')
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
    return redirect('learn')


@login_required(login_url='/learn/login')
def learn_start(request):
    user_enrollment_id = request.GET.get('id', '')

    user_enrollment = get_object_or_404(CoarseEnrollment, id=user_enrollment_id, user=request.user)
    
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
         'coarse_content': coarse_content,
         'path': MEDIA_URL
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


def filter_loans(request):
    user = request.user
    query = Q()

    # Use the user's SME registration to set the business type filter if available
    try:
        sme_registration = SMERegistration.objects.get(user=user)
        business_type = sme_registration.type_of_business
        query &= Q(business_type__icontains=business_type)
    except SMERegistration.DoesNotExist:
        # Optionally handle cases where the user does not have an SME registration
        business_type = None

    if user.income_per_month:
        min_income_required = float(user.income_per_month)
        query &= Q(min_income_required__lte=min_income_required)
    else:
        # Optionally handle cases where the user does not have an income specified
        query &= Q(min_income_required__isnull=True)

    loans = LoanService.objects.filter(query)
    user_age = calculate_age(user.date_of_birth)
    context ={
        "user":user,
        "loans":loans,
        "user_age": user_age,
        "path": MEDIA_URL
    }
    return render(request, 'loans_list.html', context)


def calculate_age(born):
    if born:
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return "Not specified"

class LoanServiceDetailView(DetailView):
    model = LoanService
    template_name = 'loan_service_detail.html'
    context_object_name = 'loan'