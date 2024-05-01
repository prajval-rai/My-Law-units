"""
URL configuration for law_units project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.user_login,name="login"),
    path('index/', views.index,name="index"),
    path('home/cases/',views.cases,name="cases"),
    path('home/NewCase/',views.newcases,name="newcases"),
    path('home/',views.home,name="home"),
    path('home/forgotpassword/',views.forgotpassword,name="forgotpassword"),
    path('home/Document/',views.document,name="doc"),
    path('home/Document/',views.newdocument,name="NewDocument"),
    path('home/CompletedToDo/',views.completedtodo,name="todo"),
    path('home/UpcomingToDo/',views.upcomingtodo,name="upcomingtodo"),
    path('home/PendingToDo/',views.pendingtodo,name="pendingtodo"),
    path('home/AllToDo/',views.alltodo,name="alltodo"),
    path('home/Dashboard/',views.Dashboard,name="Dashboard"),
    path('signup/',views.Signup),
    path('calendar/',views.Calender),
]
