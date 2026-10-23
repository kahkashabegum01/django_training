from django.urls import path
from app2 import views

urlpatterns = [
    path("instagram",views.instagram), 
    path("linkedin",views.linkedin),
]