from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')


def main(request):
    return render(request, 'main.html')


def single(request):
    return render(request, 'single.html')

def contact(request):
    return render(request,'contact.html')