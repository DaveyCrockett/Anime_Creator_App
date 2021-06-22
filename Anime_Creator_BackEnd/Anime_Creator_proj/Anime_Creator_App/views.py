from django.shortcuts import render
from django.http import HttpResponse
from .models import AnimeCreator

# Create your views here.


def index(request):
    all_creators = AnimeCreator.objects.all()
    context = {
        'all_creators': all_creators
    }
    return render(request, 'Anime_Creator_App/index.html', context)
