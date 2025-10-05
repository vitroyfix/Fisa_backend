from django.shortcuts import render
from .models import Admissions

def admissions_view(request):
    admissions_list = Admissions.objects.all()
    return render(request, "admissions.html", {"admissions": admissions_list})
