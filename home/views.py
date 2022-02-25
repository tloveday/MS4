from django.shortcuts import render
from .models import Coach

# Create your views here.


def index(request):
    """ View for index page"""
    return render(request, 'home/index.html')


def our_team(request):
    """ View for index page"""
    return render(request, 'home/our_team.html')
