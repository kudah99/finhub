from django.shortcuts import render
from coarse.models import Coarse

def index(request):

    coarses = Coarse.objects.all()
    context = {
         'coarses': coarses
     }
    return render(request, 'index.html',context)