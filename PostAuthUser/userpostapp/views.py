from django.shortcuts import render
from userpostapp.forms import UserForm,PostForm
from userpostapp.models import User,Post
  
def index(request):  
    form = PostForm()
    
     
    return render(request,"index.html",{'form':form})  