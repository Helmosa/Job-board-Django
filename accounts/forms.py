from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields

from job.models import Job
from .models import Profile

class SignupForm(UserCreationForm):   
    class Meta:
        model = User
        fields=('username','first_name','last_name','email','password1','password2')
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city','phone','image']
        
        