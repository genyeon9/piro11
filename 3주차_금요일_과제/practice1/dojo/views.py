from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def mysum(request, numbers):
    result = sum(map(lambda x:int(x or 0),numbers.split('/')))
    return HttpResponse(result)
