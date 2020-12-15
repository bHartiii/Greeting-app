from django.shortcuts import render,HttpResponse
from datetime import datetime
from greetingApp.models import Index

def index(request):
    context = {
        "variable" : "Hello!!!"
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        msg = request.POST.get('msg')
        index = Index(name=name, age=age, msg=msg, date=datetime.today())
        index.save()
    return render(request,'index.html', context)
