from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import adminSignup

# Create your views here.
def index(request):
    return render(request,'index.html')
def adminsignup(request):
    if request.method=='POST':
        fullname=request.POST['fullname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            user=User.objects.create_user(username=username,password=password1,email=email)
            user.save()
            adminSignup.objects.create(username=username,full_name=fullname,email=email,password=password1)
            return redirect('adminlogin')
        else:
            messages.info(request,'passwords doesnt match')
            return redirect('adminsignup')
    else:
        return render(request,'adminsignup.html')
def adminlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        user=auth.authenticate(username=username,email=email,password=str(password))

        if user is not None:
            auth.login(request,user)
            return render(request,'index.html')
        else:
            messages.info(request,'Username / password is incorrect')
            return redirect('adminlogin')
    else:
        return render(request,'adminlogin.html')
def usersignup(request):
    return render(request,'usersignup.html')
def userlogin(request):
    return render(request,'userlogin.html')