from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.http import require_POST

from mydata.models import user, student


# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    return render(request, 'signup.html')


def password(request):
    return HttpResponse("<h1>this is password page</h1>")


def saveuser(request):
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('signup'))

    username = request.POST.get('username')
    name = request.POST.get('name')
    password_value = request.POST.get('password')

    if not username or not name or not password_value:
        return render(request, 'signup.html', {'errormsg': 'All fields are required'})

    if user.objects.filter(username=username).exists():
        return render(request, 'signup.html', {'errormsg': 'Username is Already Exists'})

    user.objects.create(username=username, name=name, password=password_value)
    return HttpResponseRedirect(reverse('login'))


def login(request):
    return render(request, 'login.html')


@require_POST
def loginvalidation(request):
    username = request.POST.get('username')
    password_value = request.POST.get('password')

    if user.objects.filter(username=username, password=password_value).exists():
        request.session['username'] = username
        return HttpResponseRedirect(reverse('studentform'))

    return render(request, 'login.html', {'reg': 'invalid username or password'})


def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('login'))


def studentform(request):
    return render(request, 'student.html')


def studentlist(request):
    students = student.objects.all()
    return render(request, 'studentlist.html', {'students': students})


@require_POST
def savestudent(request):
    s_id = request.POST.get('s_id')
    sname = request.POST.get('sname')
    sbranch = request.POST.get('sbranch')

    if not s_id or not sname or not sbranch:
        return render(request, 'student.html', {'msg': 'All fields are required'})

    student.objects.create(s_id=s_id, sname=sname, sbranch=sbranch)
    return render(request, 'student.html', {'msg': 'Student saved successfully'})


