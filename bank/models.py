from django.db import models
from django_resized import ResizedImageField
from django.urls import reverse
from app.storage_backend import PublicMediaStorage


class FinancialServiceProvider(models.Model):
    name = models.CharField(max_length=100)
    services = models.TextField()
    logo = models.ImageField(storage=PublicMediaStorage(), null=True,blank=True)
    link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class LoanService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    service_provider = models.ForeignKey(FinancialServiceProvider, on_delete=models.CASCADE, null=True)
    business_type = models.CharField(max_length=100)
    min_loan_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    max_loan_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    eligibility_criteria = models.TextField(null=True, blank=True)
    min_income_required = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

class InvestmentService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    service_provider = models.ForeignKey(FinancialServiceProvider, on_delete=models.CASCADE, null=True)
    business_type = models.CharField(max_length=100)
    min_investment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    expected_return_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    eligibility_criteria = models.TextField(null=True, blank=True)
    min_income_required = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
