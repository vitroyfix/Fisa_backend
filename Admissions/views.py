from django.shortcuts import render
from .models import Admission

def admissions_view(request):
    admissions_list = Admission.objects.all()
    return render(request, "admissions.html", {"admissions": admissions_list})
