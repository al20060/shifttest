from django.shortcuts import render
from .models import Indiinfo

# Create your views here.
def frontpage(request):
    Indiinfos = Indiinfo.objects.all()
    return render(request, "login/frontpage.html", {"Indiinfos":Indiinfos})