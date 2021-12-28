from django.contrib.auth import authenticate, login
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from .forms import SignupForm,ProfileForm,UserForm
from .models import Profile
from django.urls import reverse
# Create your views here.

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password) # if user and email is not none ==> Create new account (Do Login)
            login(request,user)
            return redirect(reverse('accounts:profile'))
    else:
        form = SignupForm()
    return render(request,'registration/signup.html',{'form':form})


def profile(request):
    profile = Profile.objects.get(user=request.user) # هنا بجيب اليوزر الي عامل لوجن
    return render(request,'accounts/profile.html',{'profile':profile})



def profile_edit(request):
    profile_edit = Profile.objects.get(user=request.user) # هنا بجيب اليوزر الي عامل لوجن
    if request.method == 'POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile_edit)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile= profileform.save(commit=False) ## commit=false ===> to Get user And Edit Data        
            myprofile.save()
            return redirect(reverse('accounts:profile'))
    else:
        userform = UserForm(instance=request.user) # looged ueser Now
        profileform = ProfileForm(instance=profile_edit) # Data Belong to USer Looged Now
    context={'userform':userform,
             'profileform':profileform,
             }
    return render(request,'accounts/profile_edit.html',context)