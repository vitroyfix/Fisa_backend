from django.shortcuts import render
from .models import NonMember

def nonmembers_view(request):
    nonmembers = NonMember.objects.all()
    return render(request, "nonmembers.html", {"nonmembers": nonmembers})
