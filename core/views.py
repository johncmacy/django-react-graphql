from django.shortcuts import render
from .models import Thing

def index(request):
    return render(request, 'core/index.html')