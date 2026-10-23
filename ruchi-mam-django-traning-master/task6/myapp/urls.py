from django.urls import URLPattern, path
from . views import *

urlpatterns=[
    path("productlist/",productlist, name="read"),
    path("createproduct/",createproduct, name="create"),
    path("updateproduct/",updateproduct, name="update"),
    path("updateproductform/",updateproductform, name="updateform"),
    path("deleteproduct/",deleteproduct, name="delete"),
    path("newemployeeform/",newproductform, name='newemployeeform'),
]