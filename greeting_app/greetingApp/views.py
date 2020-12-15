from django.shortcuts import render,HttpResponse
from datetime import datetime
from greetingApp.models import User
from django.contrib import messages

def index(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        msg = request.POST.get('msg')
        index = User(name=name, age=age, msg=msg, date=datetime.today())
        index.save()
        messages.success(request, 'Your messgae has been sent!!!')
    return render(request,'index.html')

def show(request):
    users = User.objects.all()
    return render(request, 'show.html')
