from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'w3c.html')
def result(request):
    return render(request,'result.html')