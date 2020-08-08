from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def index(request):
    #return HttpResponse("Hey, Hi there")
    return render(request,'generator/index.html')
def password(request):
    char = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        char.extend(list('0123456789'))
    if request.GET.get('specialchar'):
        char.extend(list('!~@#%^&*()_ ,.<>/?;'))
    length=int(request.GET.get('length'))
    thepassword=''

    for i in range(length):
        thepassword+=random.choice(char)
    
    return render(request,'generator/password.html',{'password':thepassword})

def about(request):
    return render(request,'generator/about.html')