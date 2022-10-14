from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('home/<name>',views.hiname,name="hi"),
    path('add/<n1>/<n2>',views.add,name="add"),
    path('',views.temp,name="index"),
    path('grt/<a>/<b>',views.grt,name="grt"),
    path('home/',views.home,name="home"),
    path('aboutus/',views.about,name="aboutus"),
    path('base/',views.base,name="base"),
    path('register/',views.register,name="reg"),
]
