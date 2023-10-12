from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('service/',views.service,name='service'),
    path('course/',views.course,name='course'),
    path('aboutus/',views.about,name='about'),

]