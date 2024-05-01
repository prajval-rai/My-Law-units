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
    path('home/',views.home,name="home"),
    path('home/forgotpassword/',views.forgotpassword,name="forgotpassword"),
    path('home/Document/',views.document,name="doc"),
    path('home/AllToDo/',views.todo,name="todo"),
]
