
from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contactus/',views.contact,name='contact'),
    path('help/',views.help,name='help'),
    path('service/',views.service,name='service'),
]
