from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    t="<h2>Welcome to SISTec Bhopal</h2>"
    s="<h1>Sagar Institute of Science and Technology (SISTec) is a prominent group of technical and professional institutions located in Bhopal, Madhya Pradesh, established in 2007 under the Sagar Group of Institutions</h1>"
    return HttpResponse(t + s)