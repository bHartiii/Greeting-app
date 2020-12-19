import js2py
from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from greetingsApp.models import Users
from django.contrib import messages

def index(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        msg = request.POST.get('msg')
        user = Users(name=name, msg=msg, date =datetime.today())
        try:
            user.save()
            messages.success(request, 'Your messgae has been sent!!!')
        except:
            pass

    return render(request,'index.html')

def show(request):
    context = {
        "users" : Users.objects.all()
    }
    return render(request, 'show.html',context)

def update(request, id):
    userid=id
    if request.method=='POST':
        name = request.POST.get('name')
        msg = request.POST.get('msg')
        user_object = Users(name=name, msg=msg, date=datetime.today(),id=userid)
        try:
            user_object.save()
            messages.success(request, 'Your messgae has been updated!!!')
        except:
            pass
        return redirect('/show')
    else:
        context = {
            "users" : User.objects.filter(id=userid)
        }
        return render(request,'update.html',context)

def delete(request, id):
    userid=id
    user = Users.objects.get(id=userid)
    user.delete()
    return redirect('/show')
