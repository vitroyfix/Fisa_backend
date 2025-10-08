from django.shortcuts import render
from .models import Event

def events_view(request):
    events = Event.objects.prefetch_related(
        'council_participations__council_member__student'
    ).all()
    return render(request, "events.html", {"events": events})
