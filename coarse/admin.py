from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Coarse

class CoarseResource(resources.ModelResource):
    class Meta:
        model = Coarse

class CoarseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','image','name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)

    resource_class = CoarseResource

admin.site.register(Coarse, CoarseAdmin)