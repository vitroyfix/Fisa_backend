from django.shortcuts import render
from .models import Council


def council_view(request):
    all_council_members = Council.objects.all()
    return render(request, 'council_members.html', {'council_members': all_council_members})