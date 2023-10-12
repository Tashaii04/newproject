from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    data=StudentModel.objects.all()
    print(data.values())
    data1={
        'key':list(data.values())
    }
    return render(request,'app/home.html',data1)