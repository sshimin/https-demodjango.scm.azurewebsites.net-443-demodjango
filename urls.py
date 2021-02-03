from django.urls import path
from calculation import views
from calculation import view1
from calculation import basics
from calculation import prepare

urlpatterns = [
    path('',views.cal,name='calculation'),
    path('add',view1.add,name='add'),

   ]
