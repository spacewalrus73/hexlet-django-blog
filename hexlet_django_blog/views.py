from django.shortcuts import render
from django.views.generic.base import TemplateView


def index(request):
    return render(request, 'index.html')


def about(request):
    tags = ["Обучение", "программирование", "python", "oop"]
    return render(request, 'about.html', context={'tags': tags})
