from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index(request):
    return render(request, 'main_app/index.html')


def about(request):
  return render(request, 'about.html')