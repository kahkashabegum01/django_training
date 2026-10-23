from django.urls import path
from aids import views

urlpatterns = [
    path("class",views.page),
]