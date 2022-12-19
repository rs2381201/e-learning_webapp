import email
from sys import implementation
from venv import create
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def account(request):
    return HttpResponse("This is your account")


def register(request):
    if request.method=="POST":
        fname=request.POST["fn"]
        lname=request.POST["ln"]
        uname=request.POST["un"]
        email=request.POST["en"]
        ped=request.POST["pn"]
        cowd=request.POST["cpn"]
        if cowd== ped:
            usr=User.objects,create_user(first_name=fname,username=uname,last_name=lname,email=email,password=ped)
            usr.save()
            return redirect("am")
        else:
            return redirect("ab")
        
    render(request,"signup.html")

def login (request):
    if request.method=="POST":
        un=request.POST["user"]
        psd=request.POST["password"]
        usr=auth.authenticate(username=un,password=psd)
        if len(usr)>0:            
          auth.login(usr)

        return render(request,"login.html")
