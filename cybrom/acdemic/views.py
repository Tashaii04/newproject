from django.shortcuts import render

def home(req):#http request
    return render(req,"acdemic/index.html")

def about(req):#http request
    return render(req,"acdemic/about.html")

def contact(req):#http request
    return render(req,"acdemic/contact.html")

def service(req):#http request
    return render(req,"acdemic/service.html")

def help(req):#http request
    return render(req,"acdemic/help.html")
