from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('a/', views.home1),
    path('ren/',views.getbyrender),
]