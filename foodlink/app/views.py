from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request, *args, **kargs):
    return render(request, 'index.html', {})