from django.shortcuts import render
from .models import Attend

def attendances_view(request):
    attendances = Attend.objects.all()
    return render(request, "attendances.html", {"attend_list": attendances})
