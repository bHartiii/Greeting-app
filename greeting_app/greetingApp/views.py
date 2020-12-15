from django.shortcuts import render,HttpResponse

def index(request):
    context = {
        "variable" : "Hello!!!"
    }
    return render(request,'index.html', context)
