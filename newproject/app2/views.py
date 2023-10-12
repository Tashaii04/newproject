from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req,'app2/index.html')

def about(req):
    return render(req,'app2/about.html')

def service(req):
    return render(req,'app2/service.html')
def course(req):
    return render(req,'app2/course.html')

def contact(req):
    return render(req,'app2/contact.html')