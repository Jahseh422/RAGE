from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi!")

def test(request):
    return HttpResponse('Aoaoao')