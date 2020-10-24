from django.shortcuts import render
from django.http import HttpResponse

def getScore(request):
    return render(request,'home.html')
