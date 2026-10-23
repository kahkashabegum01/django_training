from django.shortcuts import render


def testpaper(request):
    context = {
        "que": "who developed python",
        "a": "Guido van Rossum",
        "b": "James Gosling",
        "c": "Dennis Ritchie",
        "d": "Bjarne Stroustrup",
    }
    return render(request, "testpaper.html", context)


def info(request):
    context = {
        "name": "Arjit",
        "age": 20,
        "city": "Bhopal",
    }
    return render(request, "info.html", context)


def sum(request):
    a = 10
    b = 20
    c = 30
    d = a + b + c
    context = {
        "a": a,
        "b": b,
        "c": c,
        "d": d,
    }
    return render(request, "add.html", context)


def result(request):
    context = {
        "name": "Arjit",
        "marks": 90,
    }
    return render(request, "result.html", context)


def voting(request):
    content = {
        "name": "Arjit",
        "age": 20,
        "country": "India",
    }
    return render(request, "voting.html", content)

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

