from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(req): 
    return HttpResponse('<h1>This is my home page</h1>')

def home1(req): 
    return HttpResponse('<h1>This is my Second page</h1>')


def getbyrender(req):
    data=[1,2,3,4,5]
    return render(req,'app1/index.html',
{'name':'Ajay','age':'25', 'address':'Bhopal','d1':data})