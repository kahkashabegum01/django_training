from django.shortcuts import render, redirect
from homework.models import testing_1, testing_2, testing_3, testing_4, SimpleUser

# Correct answers for each test and question ID
ANSWERS = {
    1: {1: 'def', 2: 'my_name', 3: '14', 4: 'List'},
    2: {1: 'Hyper Text Markup Language', 2: '<a>', 3: '<img>', 4: '<h1>'},
    3: {1: 'Structured Query Language', 2: 'SELECT', 3: 'INSERT', 4: 'DROP TABLE'},
    4: {1: 'Sun Microsystems', 2: 'class', 3: 'main()', 4: ';'}
}

def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        SimpleUser.objects.create(name=name, username=username, password=password)
        return render(request, "signup.html", {"msg": "User created successfully!"})
        
    return render(request, "signup.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = SimpleUser.objects.filter(username=username, password=password).first()
        
        if user:
            request.session["username"] = user.username
            return redirect("dashboard")
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})
            
    return render(request, "login.html")

def dashboard(request):
    username = request.session.get("username", "Student")
    return render(request, "dashboard.html", {"username": username})

def test(request, test_id):
    if test_id == 1:
        questions = testing_1.objects.all()
        test_name = "Test 1 (Python)"
    elif test_id == 2:
        questions = testing_2.objects.all()
        test_name = "Test 2 (HTML)"
    elif test_id == 3:
        questions = testing_3.objects.all()
        test_name = "Test 3 (SQL)"
    elif test_id == 4:
        questions = testing_4.objects.all()
        test_name = "Test 4 (Java)"
    else:
        return redirect("dashboard")

    context = {
        "questions": questions,
        "test_name": test_name,
        "test_id": test_id
    }
    return render(request, "test.html", context)

def result(request):
    if request.method == "POST":
        test_id = int(request.POST.get("test_id", 1))
        correct_dict = ANSWERS.get(test_id, {})
        
        right = 0
        wrong = 0
        total = len(correct_dict)
        
        for q_id, correct_ans in correct_dict.items():
            user_ans = request.POST.get(f"q_{q_id}")
            if user_ans == correct_ans:
                right += 1
            else:
                wrong += 1
                
        context = {
            "total": total,
            "right": right,
            "wrong": wrong
        }
        return render(request, "result.html", context)

    return redirect("dashboard")
