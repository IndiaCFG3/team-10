from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import adminSignup,userSignup

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
        x=User.objects.all()
        l=[]
        for x1 in x:
            l.append(x1.username)
        if password1==password2:
            if username not in l:
                user=User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                adminSignup.objects.create(username=username,full_name=fullname,email=email,password=password1)
                return redirect('adminlogin')
            else:
                messages.info(request,'username already exists')
                return redirect('adminsignup')
        
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
        a1=adminSignup.objects.all()
        l=[]
        for a in a1:
            l.append(a.username)
        if user is not None:
            if username in l:
                auth.login(request,user)
                return render(request,'index.html')
            else:
                messages.info(request,'you are not an admin')
                return redirect('adminlogin')
        else:
            messages.info(request,'Username / password is incorrect')
            return redirect('adminlogin')
    else:
        return render(request,'adminlogin.html')
def usersignup(request):
    if request.method=='POST':
        fullname=request.POST['fullname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        l=[]
        x=User.objects.all()
        for x1 in x:
            l.append(x1.username)
        if password1==password2:
            if username not in l:
                user=User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                userSignup.objects.create(username=username,full_name=fullname,email=email,password=password1)
                return redirect('userlogin')
            else:
                messages.info(request,'username already exists')
                return redirect('usersignup')
        else:
            messages.info(request,'passwords doesnt match')
            return redirect('usersignup')
    else:
        return render(request,'usersignup.html')
def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        user=auth.authenticate(username=username,email=email,password=str(password))
        u1=userSignup.objects.all()
        l=[]
        for u in u1:
            l.append(u.username)
        if user is not None:
            if username in l:
                auth.login(request,user)
                return render(request,'index.html')
            else:
                messages.info(request,'you are not a user')
                return redirect('userlogin')
        else:
            messages.info(request,'Username / password /email is incorrect')
            return redirect('userlogin')
    else:
        return render(request,'userlogin.html')