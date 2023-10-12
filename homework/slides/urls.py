from django.urls import path
from . import views             #.dot means same dirictory

urlpatterns = [
    path('',views.home,name='home'),
    path('insert/',views.insert,name='insert'),
    path('record/',views.record,name='record'),
    path('update/',views.update,name='update'),
    path('delete/',views.delete,name='delete')
]