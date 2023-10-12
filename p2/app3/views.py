from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req,'app3/index.html')

def about(req):
    return render(req,'app3/about.html')

def fees(req):
    return render(req,'app3/fees.html')

def panelty(req):
    return render(req,'app3/panelty.html')

def contact(req):
    return render(req,'app3/contact.html')