from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.



def register(request):
    form= UserCreationForm(request.POST)
    context={'form':form}
    return render(request,"signUp.html",context)

def connect(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,"login.html",{})
