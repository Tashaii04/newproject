from django.shortcuts import render

# Create your views here.


def home2(req):
    return render(req,'app2/home2.html')