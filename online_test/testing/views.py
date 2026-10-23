from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Test, Question
from django.urls import reverse

def home_page(request):
    res = render(request, 'home.html')
    return res


def signup(request):
    res = render(request, 'signup.html')
    return res


def saveuser(request):
    username = request.POST['username']
    password = request.POST['password']
    name = request.POST['name']

    user = User(
        username=username,
        password=password,
        name=name
    )
    user.save()

    url = reverse('signup_success')
    return HttpResponseRedirect(url)


def signup_success(request):
    res = render(request, 'signup_success.html')
    return res


def login(request):
    res = render(request, 'login.html')
    return res


def checklogin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = User.objects.filter(username=username, password=password)

    if user:
        request.session['username'] = username
        return HttpResponseRedirect(reverse('tests'))
    else:
        return HttpResponseRedirect(reverse('login'))


def addtests(request):
    test1 = Test(subject='Python', total_questions=3)
    test1.save()

    test2 = Test(subject='Data Science', total_questions=5)
    test2.save()

    test3 = Test(subject='Django', total_questions=10)
    test3.save()

    return HttpResponse("Tests saved successfully")


def tests(request):

    username = request.session.get('username')

    res = render(request, 'tests.html', {
        'username': username
    })

    return res

def python_test(request):
    questions = Question.objects.filter(subject='Python')
    res = render(request, 'python_test.html', {'questions': questions})
    return res


def submit_python_test(request):

    q1 = Question.objects.filter(id=1).values()
    q2 = Question.objects.filter(id=2).values()
    q3 = Question.objects.filter(id=3).values()

    score = 0

    if request.POST['q1'] == q1[0]['answer']:
        score = score + 1

    if request.POST['q2'] == q2[0]['answer']:
        score = score + 1

    if request.POST['q3'] == q3[0]['answer']:
        score = score + 1

    username = request.session.get('username')
    res = render(request, 'result.html', {
        'score': score,
        'subject': 'Python',
        'total': 3,
        'username': username
    })
    return res


def data_science_test(request):
    questions = Question.objects.filter(subject='Data Science')
    res = render(request, 'data_science_test.html', {'questions': questions})
    return res

def submit_data_science_test(request):

    q1 = Question.objects.filter(id=4).values()
    q2 = Question.objects.filter(id=5).values()
    q3 = Question.objects.filter(id=6).values()
    q4 = Question.objects.filter(id=7).values()
    q5 = Question.objects.filter(id=8).values()

    score = 0

    if request.POST['q4'] == q1[0]['answer']:
        score = score + 1

    if request.POST['q5'] == q2[0]['answer']:
        score = score + 1

    if request.POST['q6'] == q3[0]['answer']:
        score = score + 1

    if request.POST['q7'] == q4[0]['answer']:
        score = score + 1

    if request.POST['q8'] == q5[0]['answer']:
        score = score + 1

    username = request.session.get('username')
    res = render(request, 'result.html', {
        'score': score,
        'subject': 'Data Science',
        'total': 5,
        'username': username
    })

    return res

def django_test(request):

    questions = Question.objects.filter(subject='Django')

    res = render(request, 'django_test.html', {'questions': questions})
    return res

def submit_django_test(request):

    q1 = Question.objects.filter(id=9).values()
    q2 = Question.objects.filter(id=10).values()
    q3 = Question.objects.filter(id=11).values()
    q4 = Question.objects.filter(id=12).values()
    q5 = Question.objects.filter(id=13).values()

    score = 0

    if request.POST['q9'] == q1[0]['answer']:
        score = score + 1

    if request.POST['q10'] == q2[0]['answer']:
        score = score + 1

    if request.POST['q11'] == q3[0]['answer']:
        score = score + 1

    if request.POST['q12'] == q4[0]['answer']:
        score = score + 1

    if request.POST['q13'] == q5[0]['answer']:
        score = score + 1

    username = request.session.get('username')
    res = render(request, 'result.html', {
        'score': score,
        'subject': 'Django',
        'total': 5,
        'username': username
    })

    return res
