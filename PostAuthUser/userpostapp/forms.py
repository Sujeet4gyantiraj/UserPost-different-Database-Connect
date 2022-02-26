from django import forms  
from userpostapp.models import User,Post
  
class UserForm(forms.ModelForm):  
    class Meta:  
        model = User  
        fields = ['user','email','password'] 

class PostForm(forms.ModelForm):  
    class Meta:  
        model = Post 
        fields = "__all__"  