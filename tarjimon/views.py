from django.shortcuts import render
from .models import Lugat

# Create your views here.

def index(request):
    soz = request.GET.get('q','')
    soz = soz.strip()
    soz = soz.lower()
    if soz and soz != '':
        natija = Lugat.objects.filter(inglizcha__contains=soz).all()[:3]
    else:
        natija = None

    return render(request,'index.html',{'q':soz,'natija': natija})