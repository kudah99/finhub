from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import CustomUser

class CustomUserResource(resources.ModelResource):
    class Meta:
        model = CustomUser

class CustomUserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('username','first_name','last_name','gender','date_of_birth','occupation','business_owner','income_per_month')
    search_fields = ('username',)

    resource_class = CustomUserResource

admin.site.register(CustomUser, CustomUserAdmin)
