from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def instagram(request):
    s1="<h1> my instagram profile </h1>"
    return HttpResponse(s1)

def linkedin(request):
    s2="<h1> my linkedin profile </h1>"
    return HttpResponse(s2)