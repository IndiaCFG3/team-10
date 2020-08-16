from django.urls import path
from .import views

urlpatterns=[
    path('', views.index,name="index"),
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('adminsignup',views.adminsignup,name='adminsignup'),
    path('usersignup',views.usersignup,name='usersignup'),
    path('userlogin',views.userlogin,name='userlogin'),
]