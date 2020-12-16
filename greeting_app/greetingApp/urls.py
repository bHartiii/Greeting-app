from django.contrib import admin
from django.urls import path
from greetingApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show',views.show, name='show'),
    path('update/<int:id>',views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]
