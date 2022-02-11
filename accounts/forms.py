from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields

from job.models import Job
from .models import Profile,NameComapny

## Registration ##
class SignupForm(UserCreationForm):   ## دا للناس الي عايزه تشتغل    
    class Meta:
        model = User
        fields=('username','first_name','last_name','email','password1','password2')
#########################################
## Registation Form_CO##

class SignupForm2(UserCreationForm):   ## دا للناس الي عايزه ناس تشتغل
    class Meta:
        model = User
        fields=('username','first_name','last_name','email','password1','password2')
                
class ComanyForm(forms.ModelForm):
     class Meta:
         model = NameComapny
         fields = ['Company_Name']               


#########################################                
## update Profile ##
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city','phone','image','company_Name','User_Type']
##############################################

class AddJobDashboard(forms.ModelForm):
    class Meta:
       model = Job
       fields = ['title']
