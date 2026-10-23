import joblib
from pathlib import Path

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

BASE_DIR = Path(__file__).resolve().parent.parent


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')


def result(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        return render(request, 'home.html', {'error': 'Please submit the form.'})

    feature_names = ['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']
    values = []

    for field in feature_names:
        value = request.POST.get(field)
        if value is None or value == '':
            return render(request, 'home.html', {'error': 'Please fill in all fields.'})
        try:
            values.append(float(value))
        except ValueError:
            return render(request, 'home.html', {'error': 'All values must be numeric.'})

    scaler = joblib.load(BASE_DIR / 'scalermodel.pkl')
    mlmodel = joblib.load(BASE_DIR / 'mlmodel.pkl')

    scaled_input = scaler.transform([values])
    ans = int(mlmodel.predict(scaled_input)[0])

    return render(request, 'result.html', {'ans': ans, 'lis': values})
