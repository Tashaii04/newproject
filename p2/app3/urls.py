from django.urls import path
from . import views

urlpatterns = [

    path('' ,views.home,name='home'),
    path('about',views.about,name='about'),
    path('fees' ,views.fees,name='fees'),
    path('panelty' ,views.panelty,name='panelty'),
    path('contact' ,views.contact,name='contact'),
    
]