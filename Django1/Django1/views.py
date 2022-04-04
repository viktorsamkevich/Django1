from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request,'about.html', {'gretting': 'hello'})

def reverse(request):
    user_text = request.GET['username']
    reverse = user_text[::-1]
    return render(request,'reverse.html',{'word': reverse})

def home(request):
    return render(request, 'home.html')
    return HttpResponse('This is my home')