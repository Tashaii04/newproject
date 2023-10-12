from django.shortcuts import render
from .models import Student

def home(req):
    return render(req,'app1/index.html')

def insert(req):
    if req.method=='POST':
         print(req.POST)
         fn=req.POST.get('fn')
         ln=req.POST.get('ln')
         age=req.POST.get('ag')
         email=req.POST.get('em')
         image=req.FILES.get('im')
         data=Student(name=fn,lname=ln,age=age,email=email,image=image)
         data.save()

    return render(req,'app1/insert.html')

def display(req):
        return render(req,'app1/display.html')
