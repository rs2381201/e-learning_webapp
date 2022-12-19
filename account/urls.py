from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
path("",views.register,name="reg")
path("log",views.login,name="log",)
]