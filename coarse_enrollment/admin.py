from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import CoarseEnrollment

class CoarseEnrollmentResource(resources.ModelResource):
    class Meta:
        model = CoarseEnrollment

class CoarseEnrollmentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','user', 'coarse','status','progress', 'last_content_accessed', 'updated_at')
    search_fields = ('coarse',)

    resource_class = CoarseEnrollmentResource

admin.site.register(CoarseEnrollment, CoarseEnrollmentAdmin)
