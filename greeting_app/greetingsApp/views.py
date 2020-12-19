import js2py
from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from greetingsApp.models import Users
from django.contrib import messages

#counter = 'function getNextSequenceValue(sequenceName){var sequenceDocument = db.findAndModify({query:{_id: sequenceName },update: {$inc:{sequence_value:1}},new:true});return sequenceDocument.sequence_value;}'


def index(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        msg = request.POST.get('msg')
        # userid = User.objects.all().count()+1
        user = Users(name=name, msg=msg, date =datetime.today())
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
    user = User.objects.get(id=userid)
    user.delete()
    return redirect('/show')
