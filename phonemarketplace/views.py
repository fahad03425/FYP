from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse("hello world, you are watcing afahad")
    return render(request,'index.html')
