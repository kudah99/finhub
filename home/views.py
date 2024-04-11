from django.shortcuts import render
from coarse.models import Coarse
from home.models import SiteDetails
from app.settings import MEDIA_URL

def index(request):

    coarses = Coarse.objects.all()
    site_details = SiteDetails.objects.all().first()
    logo_url = MEDIA_URL
    context = {
         'coarses': coarses,
         'site_details': site_details,
         'logo_url': logo_url
     }
    return render(request, 'index.html',context)