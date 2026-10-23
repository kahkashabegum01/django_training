from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("home/", views.home, name='home2'),
    path("signup/", views.signup, name='signup'),
    path("saveuser/", views.saveuser, name='saveuser'),
    path("login/", views.login, name='login'),
    path("loginvalidation/", views.loginvalidation, name='loginvalidation'),
    path("logout/", views.logout, name='logout'),
    path("studentform/", views.studentform, name='studentform'),
    path("savestudent/", views.savestudent, name='savestudent'),
    path("studentlist/", views.studentlist, name='studentlist'),
]