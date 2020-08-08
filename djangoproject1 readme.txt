django-admin startproject nameoftheproject
django-admin startproject passowrd_generator
cd password_generator/python manage.py runserver
django apps:
inside one project we can have multiple apps
inside password-generator-project: python manage.py startapp generator
now generator is our app inside top level project password-generator
#displaying our own content on page and removing admin page

step1-: Go to the password_generator>urls.py
#from django.contrib import admin
from django.urls import path
from generator import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home),
]

Step2: Go to the app i.e generator>views.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hey, Hi there")
________________________________________________________________
How to add our own html page
step-1 create folder templates in generator(our_app)>generator>index.html
index.html
<h1> hello iam index.html</h1>
{{name}}

Step2: Go to the app i.e generator>views.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("Hey, Hi there")
    return render(request,'generator/index.html',{'name':'Suleman'}) #dictonary