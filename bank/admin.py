from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Bank,FinancialServiceCategory

class BankResource(resources.ModelResource):
    class Meta:
        model = Bank

class FinancialServiceCategoryResource(resources.ModelResource):
    class Meta:
        model = FinancialServiceCategory

class BankAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','logo','name', 'services','link', 'created_at', 'updated_at')
    search_fields = ('name',)

    resource_class = BankResource

class FinancialServiceCategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'desscription')
    search_fields = ('name',)

    resource_class = FinancialServiceCategoryResource

admin.site.register(Bank, BankAdmin)
admin.site.register(FinancialServiceCategory, FinancialServiceCategoryAdmin)