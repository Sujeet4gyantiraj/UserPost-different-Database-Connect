from django.contrib import admin
from django.urls import path,include
from userpostapp import views

urlpatterns = [
     path('', views.index),  
    
]
