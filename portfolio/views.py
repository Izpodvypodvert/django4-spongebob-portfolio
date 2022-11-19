from django.shortcuts import render
from .models import *


def index(request):
    posts = Project.objects.all()
    return render(request, 'portfolio/index.html', context={'posts': posts})
