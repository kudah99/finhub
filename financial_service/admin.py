from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import FinancialServiceProvider, LoanService, InvestmentService

# Resource classes for django-import-export
class FinancialServiceProviderResource(resources.ModelResource):
    class Meta:
        model = FinancialServiceProvider

class LoanServiceResource(resources.ModelResource):
    class Meta:
        model = LoanService

class InvestmentServiceResource(resources.ModelResource):
    class Meta:
        model = InvestmentService

# Admin classes
class FinancialServiceProviderAdmin(ImportExportModelAdmin):
    resource_class = FinancialServiceProviderResource
    list_display = ['name', 'link', 'created_at', 'updated_at']
    search_fields = ['name']
    list_filter = ['created_at', 'updated_at']

class LoanServiceAdmin(ImportExportModelAdmin):
    resource_class = LoanServiceResource
    list_display = ['name', 'service_provider', 'business_type', 'min_loan_amount', 'max_loan_amount', 'interest_rate']
    search_fields = ['name', 'business_type', 'service_provider__name']
    list_filter = ['business_type', 'service_provider']

class InvestmentServiceAdmin(ImportExportModelAdmin):
    resource_class = InvestmentServiceResource
    list_display = ['name', 'service_provider', 'business_type', 'min_investment', 'expected_return_rate']
    search_fields = ['name', 'business_type', 'service_provider__name']
    list_filter = ['business_type', 'service_provider']

# Register your models here
admin.site.register(FinancialServiceProvider, FinancialServiceProviderAdmin)
admin.site.register(LoanService, LoanServiceAdmin)
admin.site.register(InvestmentService, InvestmentServiceAdmin)
