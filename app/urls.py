from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

admin.site.site_header  =  "FinHub Admin Panel"  
admin.site.site_title  =  "FinHub Admin Panel"
admin.site.index_title  =  "FinHub  APP"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learn/', include('student.urls')),
    path('', include('home.urls')),
    path("__reload__/", include("django_browser_reload.urls"))
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
