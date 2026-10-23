from django.urls import URLPattern, path
from . views import *

urlpatterns=[
    path("saveuser/",saveuser,name='saveuser'),
    path("employeelist/",employeelist,name='employeelist'),
    path("updateemployee/",updateemployee,name='updateemployee'),
    path("deleteemployee/",deleteemployee,name='deleteemployee'),
    path("newemployeeform/",newemployeeform,name='newemployeeform'),
    path("ateemployeeform/",updateemployeeform,name='ateemployeeform'),
    
]