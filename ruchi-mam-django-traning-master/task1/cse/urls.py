from django.urls import path
from cse import views

urlpatterns = [
    path("about",views.about),
]