from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    s="<h1>i am arjit tripathi from bhopal mp</h1>"
    return HttpResponse(s)

def about(request):
    s="<h1> my college name is sagar institure of science </h1>"
    return HttpResponse(s)