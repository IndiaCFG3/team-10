from django.urls import path
from .import views

urlpatterns=[
    path('', views.index,name="index"),
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('adminsignup',views.adminsignup,name='adminsignup'),
    path('usersignup',views.usersignup,name='usersignup'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('main',views.main,name='main'),
    path('profile',views.profile,name='profile'),
    path('schedule',views.schedule,name='schedule'),
    path('logout',views.logout,name='logout'),
    path('coursedetails',views.coursedetails,name='coursedetails'),
    path('main1',views.main1,name='main1'),
    path('html',views.html,name='html'),
    path('css',views.css,name='css'),
    path('nodejs',views.nodejs,name='nodejs'),
    path('raspberry',views.raspberry,name='raspberry'),
    path('thermodynamics',views.thermodynamics,name='thermodynamics'),
    path('others',views.others,name='others')


]