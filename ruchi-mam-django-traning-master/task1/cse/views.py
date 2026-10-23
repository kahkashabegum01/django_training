from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    t="<h2>this is cse page</h2>"
    s="<h1>The B.Tech in Artificial Intelligence and Data Science (AI&DS) at SISTec Bhopal is a four-year, AICTE-approved undergraduate program affiliated with RGPV. The curriculum blends core computer science engineering with advanced technologies like machine learning</h1>"
    return HttpResponse(t + s)
# Create your views here.
