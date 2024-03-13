from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Student

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student

class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user',)

    resource_class = StudentResource

admin.site.register(Student, StudentAdmin)
