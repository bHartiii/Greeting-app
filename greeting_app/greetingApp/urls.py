from django.contrib import admin
from django.urls import path
from greetingApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show',views.show, name='show'),
]
