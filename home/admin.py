from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import SiteDetails

class SiteDetailsResource(resources.ModelResource):
    class Meta:
        model = SiteDetails

class SiteDetailsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','logo','name')
    search_fields = ('name',)

    resource_class = SiteDetailsResource

admin.site.register(SiteDetails, SiteDetailsAdmin)