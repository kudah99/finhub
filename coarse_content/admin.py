from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import CoarseContent

class CoarseContentResource(resources.ModelResource):
    class Meta:
        model = CoarseContent

class CoarseContentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','name', 'notes','video','coarse', 'created_at', 'updated_at')
    search_fields = ('name',)

    resource_class = CoarseContentResource

admin.site.register(CoarseContent, CoarseContentAdmin)
