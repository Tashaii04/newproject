from django.urls import path,include

urlpatterns = [
    path('',include('slides.urls')),
]
from django.shortcuts import render

# Create your views here.
def home(req): #http request
    return render(req,"slides/index.html")

def insert(req):
    return render(req,"slides/insert.html")

def record(req):
    return render(req,"slides/record.html")

def update(req):
    return render(req,"slides/update.html")

def delete(req):
    return render(req,"slides/delete.html")

