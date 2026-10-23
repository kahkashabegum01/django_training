from pathlib import Path

import joblib
from django.shortcuts import redirect, render

from .models import student

BASE_DIR = Path(__file__).resolve().parent.parent


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        sid = request.POST.get('sid')
        sname = request.POST.get('sname')
        password = request.POST.get('password')
        branch = request.POST.get('branch')

        if sid and sname and password and branch:
            student.objects.create(sid=sid, sname=sname, password=password, branch=branch)
            return redirect('login')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        sid = request.POST.get('sid')
        password = request.POST.get('password')

        s = student.objects.filter(sid=sid, password=password).first()
        if s is not None:
            return render(request, 'prediction.html', {'sname': s.sname})

        return render(request, 'login.html', {'error': 'Invalid ID or password'})

    return render(request, 'login.html')


def prediction(request):
    if request.method == 'POST':
        sname = request.POST.get('sname')
        iq = request.POST.get('iq')
        cgpa = request.POST.get('cgpa')

        if iq is None or cgpa is None or iq == '' or cgpa == '':
            return render(request, 'prediction.html', {'sname': sname, 'error': 'Please enter IQ and CGPA'})

        try:
            iq_value = float(iq)
            cgpa_value = float(cgpa)
        except ValueError:
            return render(request, 'prediction.html', {'sname': sname, 'error': 'IQ and CGPA must be numeric'})

        scaler = joblib.load(BASE_DIR / 'scalermodel2.pkl')
        model = joblib.load(BASE_DIR / 'mlmodel2.pkl')

        profile_score = iq_value + (cgpa_value * 10)
        result = model.predict(scaler.transform([[cgpa_value, iq_value, profile_score]]))[0]

        # As requested, show all results as NOT PASS
        status = 'NOT PASS'

        return render(request, 'prediction.html', {'sname': sname, 'iq': iq_value, 'cgpa': cgpa_value, 'status': status})

    return render(request, 'prediction.html')


