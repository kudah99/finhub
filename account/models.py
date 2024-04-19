from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    reason = (
        ('To gain financial literacy', 'To gain financial literacy'),
        ('To access financial service', 'To access financial service')
    )
    gender = models.CharField("gender", max_length=50, choices=gender_choices, null=True)
    date_of_birth = models.DateField("date of birth", null=True)
    occupation = models.CharField(max_length=50, null=True)
    business_owner = models.BooleanField("business owner", null=True, blank=True)
    income_per_month = models.CharField(max_length=50, null=True)  
    reason_for_signup = models.CharField("reason for signup", max_length=50, choices=reason, null=True)
    financial_goals = models.TextField(null=True, blank=True)

class SMERegistration(models.Model):
    type_of_business_choice = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    )
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    business_name = models.CharField(max_length=50, null=True)
    business_id =models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    type_of_business = models.CharField(max_length=50, choices=type_of_business_choice, null=True)
    date_of_establishment = models.DateField("date of establishment", null=True)
    