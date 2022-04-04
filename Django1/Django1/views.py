from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request,'about.html', {'gretting': 'hello'})


def home(request):
    return render(request, 'home.html')
    return HttpResponse('This is my home')