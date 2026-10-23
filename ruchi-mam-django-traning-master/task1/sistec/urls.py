from django.urls import path
from sistec import views

urlpatterns = [
    path("home",views.home),
]