from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from greetingApp.models import User
from django.contrib import messages

def index(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        msg = request.POST.get('msg')
        userid = User.objects.all().count()+1
        user = User(name=name, msg=msg, date =datetime.today(), id =userid)
        try:
            user.save()
            messages.success(request, 'Your messgae has been sent!!!')
        except:
            pass

    return render(request,'index.html')

def show(request):
    context = {
        "users" : User.objects.all()
    }
    return render(request, 'show.html',context)

def update(request, id):
    userid=id
    if request.method=='POST':
        name = request.POST.get('name')
        msg = request.POST.get('msg')
        user_object = User(name=name, msg=msg, date=datetime.today(),id=userid)
        user_object.save()
        #messages.success(request, 'Your messgae has been updated!!!')
        return redirect('/show')
    else:
        context = {
            "users" : User.objects.filter(id=userid)
        }
        return render(request,'update.html',context)

def delete(request, id):
    userid=id
    user = User.objects.get(id=userid)
    user.delete()
    return redirect('/show')
