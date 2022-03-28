# users/forms.py
from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm 
from .models import CustomUser 
 
class CustomUserCreationForm(UserCreationForm):    
    class Meta:        
        model = CustomUser        
        fields = ('email', 'name', 'address', 'pv', )  
        
class CustomUserChangeForm(UserChangeForm):    
    class Meta:        
        model = CustomUser        
        fields = ('email', 'name', 'address', 'pv', )  