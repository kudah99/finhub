from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UsernameField, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from account.models import CustomUser,SMERegistration
from .widgets import INPUT_CLASSES,CHECKBOX_LABEL_CLASSES

class RegistrationForm(UserCreationForm):
  
  def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['business_owner'].required = False

  password1 = forms.CharField(
      label=_("Password"),
      widget=forms.PasswordInput(attrs={'class': 'text-sm focus:shadow-soft-primary-outline leading-5.6 ease-soft block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding py-2 px-3 font-normal text-gray-700 transition-all focus:border-fuchsia-300 focus:bg-white focus:text-gray-700 focus:outline-none focus:transition-shadow', 'placeholder': 'Password'}),
  )
  password2 = forms.CharField(
      label=_("Password Confirmation"),
      widget=forms.PasswordInput(attrs={'class': 'text-sm focus:shadow-soft-primary-outline leading-5.6 ease-soft block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding py-2 px-3 font-normal text-gray-700 transition-all focus:border-fuchsia-300 focus:bg-white focus:text-gray-700 focus:outline-none focus:transition-shadow', 'placeholder': 'Password Confirmation'}),
  )
  class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'username', 'email', 'gender', 'date_of_birth',
            'occupation', 'business_owner', 'income_per_month', 'reason_for_signup', 'financial_goals'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': " ".join(INPUT_CLASSES), 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': " ".join(INPUT_CLASSES), 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class': " ".join(INPUT_CLASSES), 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': " ".join(INPUT_CLASSES), 'placeholder': 'Email'}),
            'gender': forms.Select(attrs={'class': " ".join(INPUT_CLASSES), 'placeholder': 'Email'}),
            'date_of_birth': forms.DateInput(attrs={'class': " ".join(INPUT_CLASSES), 'placeholder': 'date of birth YYYY-MM-DD', 'type': 'date'}),
            'occupation': forms.TextInput(attrs={'class': " ".join(INPUT_CLASSES), 'placeholder': 'Occupation'}),
            'business_owner': forms.CheckboxInput(attrs={'class': " ".join(CHECKBOX_LABEL_CLASSES)}),
            'income_per_month': forms.TextInput(attrs={'class': " ".join(INPUT_CLASSES), 'placeholder': 'Income per Month'}),
            'reason_for_signup': forms.Select(attrs={'class': " ".join(INPUT_CLASSES),'placeholder': 'Income per Month'}),
            'financial_goals': forms.TextInput(attrs={'class': " ".join(INPUT_CLASSES), 'placeholder': 'Financial Goals'}),
        }

class LoginForm(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs={"class": "focus:shadow-soft-primary-outline text-sm leading-5.6 ease-soft block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 transition-all focus:border-fuchsia-300 focus:outline-none focus:transition-shadow", "placeholder": "Username"}))
  password = forms.CharField(
      label=_("Password"),
      strip=False,
      widget=forms.PasswordInput(attrs={"class": "focus:shadow-soft-primary-outline text-sm leading-5.6 ease-soft block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 transition-all focus:border-fuchsia-300 focus:outline-none focus:transition-shadow", "placeholder": "Password"}),
  )

class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'focus:shadow-soft-primary-outline text-sm leading-5.6 ease-soft block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 transition-all focus:border-fuchsia-300 focus:outline-none focus:transition-shadow',
        'placeholder': 'Email'
    }))

class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'focus:shadow-soft-primary-outline text-sm leading-5.6 ease-soft block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 transition-all focus:border-fuchsia-300 focus:outline-none focus:transition-shadow', 'placeholder': 'New Password'
    }), label="New Password")
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'focus:shadow-soft-primary-outline text-sm leading-5.6 ease-soft block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 transition-all focus:border-fuchsia-300 focus:outline-none focus:transition-shadow', 'placeholder': 'Confirm New Password'
    }), label="Confirm New Password")
    

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'focus:shadow-soft-primary-outline text-sm leading-5.6 ease-soft block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 transition-all focus:border-fuchsia-300 focus:outline-none focus:transition-shadow', 'placeholder': 'Old Password'
    }), label='Old Password')
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'focus:shadow-soft-primary-outline text-sm leading-5.6 ease-soft block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 transition-all focus:border-fuchsia-300 focus:outline-none focus:transition-shadow', 'placeholder': 'New Password'
    }), label="New Password")
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'focus:shadow-soft-primary-outline text-sm leading-5.6 ease-soft block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 transition-all focus:border-fuchsia-300 focus:outline-none focus:transition-shadow', 'placeholder': 'Confirm New Password'
    }), label="Confirm New Password")

class SMERegistrationForm(forms.ModelForm):
    class Meta:
        model = SMERegistration
        fields = ['business_name', 'business_id', 'email', 'type_of_business', 'date_of_establishment']
        widgets = {
            'business_name': forms.TextInput(attrs={'class': " ".join(INPUT_CLASSES), 'placeholder': 'Business Name'}),
            'business_id': forms.TextInput(attrs={'class': " ".join(INPUT_CLASSES), 'placeholder': 'Business ID'}),
            'email': forms.EmailInput(attrs={'class': " ".join(INPUT_CLASSES), 'placeholder': 'Business Email'}),
            'type_of_business': forms.Select(attrs={'class': " ".join(INPUT_CLASSES)}),
            'date_of_establishment': forms.DateInput(attrs={'class': " ".join(INPUT_CLASSES), 'placeholder': 'Date of Establishment', 'type': 'date'}),
        }