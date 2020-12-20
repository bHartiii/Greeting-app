import logging
from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from greetingsApp.models import Users
from django.contrib import messages
logger = logging.getLogger('django')

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
    logger.info("New user is added to greeting database.")
    return render(request,'index.html')

def show(request):
    context = {
        "users" : Users.objects.all()
    }
    logger.info("All data is fetched from greeting database.")
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
        logger.info(f"data for user id {userid} is updated in greeting databse ")
        return redirect('/show')
    else:
        context = {
            "users" : Users.objects.filter(id=userid)
        }
        logger.info(f"Update page is rendered for user {userid}.")
        return render(request,'update.html',context)

def delete(request, id):
    userid=id
    user = Users.objects.get(id=userid)
    user.delete()
    logger.info(f"user{userid} is deleted from greeting database.")
    return redirect('/show')
