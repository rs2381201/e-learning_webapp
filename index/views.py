from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from. models import *
# Create your views here.
def index(request):
    dic={}
    obj=service.objects.all()
    dic["ser"]=obj
    return render(request,"index.html",dic)

def about(request):
    return render(request,"about.html")

def courses(request):
    dic={}
    obj=service.objects.all()
    dic["ser"]=obj
    return render(request,"courses.html",dic)

def coursescat(request,pk):
    dic={}
    ct=Category.objects.get(id=pk)
    obj=service.objects.filter(catg=ct)
    dic["ser"]=obj
    return render(request,"courses.html",dic)
    
def contact(request):
    return render(request,"contact.html")
 
