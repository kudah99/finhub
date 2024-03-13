from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Bank

class BankResource(resources.ModelResource):
    class Meta:
        model = Bank

class BankAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','logo','name', 'services','link', 'created_at', 'updated_at')
    search_fields = ('name',)

    resource_class = BankResource

admin.site.register(Bank, BankAdmin)