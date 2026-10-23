from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greeting(request):
    s="<h1>i am arjit tripathi from bhopal mp</h1>"
    return HttpResponse(s)

def college(request):
    s="<h1> my college name is sagar institure of science </h1>"
    return HttpResponse(s)

def department(request):
    s="<h1> my department name is computer science </h1>"
    return HttpResponse(s)
