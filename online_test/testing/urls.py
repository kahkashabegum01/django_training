from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page, name='home'),
    path('signup/', views.signup, name='signup'),
    path('saveuser/', views.saveuser, name='saveuser'),
    path('signup-success/', views.signup_success, name='signup_success'),
    path('login/', views.login, name='login'),
    path('checklogin/', views.checklogin, name='checklogin'),
    path('addtests/', views.addtests, name='addtests'),
    path('tests/', views.tests, name='tests'),
    path('python-test/', views.python_test, name='python_test'),
    path('submit-python-test/', views.submit_python_test, name='submit_python_test'),
    path('data-science-test/', views.data_science_test, name='data_science_test'),
    path('submit-data-science-test/', views.submit_data_science_test, name='submit_data_science_test'),
    path('django-test/', views.django_test, name='django_test'),
    path('submit-django-test/', views.submit_django_test, name='submit_django_test'),
]