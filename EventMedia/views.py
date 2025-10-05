from django.shortcuts import render
from .models import Media


def media_list_view(request):
	media_list = Media.objects.all()
	return render(request, 'media_list.html', {'media_list': media_list})
