from unicodedata import name
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User, auth

from job.form import ApplyForm
from .forms import SignupForm,SignupForm2,ProfileForm,UserForm,ComanyForm,AddJobDashboard
from .models import Profile
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from job.models import Job,ApllayJob
# Create your views here.

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password) # if user and email is not exist ==> Create new account (Do Login)
            messages.success(request,f'Hi {username},Your Account Was Created Successfully!')
            login(request,user)  # Do login with New Sessions
            
            return redirect(reverse('accounts:profile'))
    else:
        form = SignupForm()
    return render(request,'registration/signup.html',{'form':form})

########
def signupCo(request):
    if request.method == "POST":
        form2 = SignupForm2(request.POST)
        namecomapny = ComanyForm(request.POST)
        if form2.is_valid() and namecomapny.is_valid():
            form2.save()
            namecomapny.save()
            username = form2.cleaned_data['username']
            password = form2.cleaned_data['password1']
            user = authenticate(username=username,password=password) # if user and email is not none ==> Create new account (Do Login)
            login(request,user)
            return redirect(reverse('accounts:profile'))
    else:
        form2 = SignupForm2()
        namecomapny = ComanyForm()
    return render(request,'registration/signup_CO.html',{'form2':form2,'namecomapny':namecomapny})

########
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
            messages.success(request, 'Your Profile has been Updated Successfully!')
            return redirect(reverse('accounts:profile'))
    else:
        userform = UserForm(instance=request.user) # looged user Now
        profileform = ProfileForm(instance=profile_edit) # Data Belong to USer Looged Now
    context={'userform':userform,
             'profileform':profileform,
             }
    return render(request,'accounts/profile_edit.html',context)



@login_required
def dashboard(request): #Have Different Information based on The Type Of User
    job_list = Job.objects.all()
    context={'userprofile': request.user.userprofile,
             'jobs':job_list}
    return render(request,'accounts/dashboard.html',context)


@login_required
def view_application(request,application_id):
    if request.user.userprofile.User_Type == 'Job Seeker':
        application = get_object_or_404(ApllayJob,pk=application_id,created_by = request.user)
    else:
        application = get_object_or_404(ApllayJob,pk=application_id,created_by = request.user)
    return render(request,'accounts/applications.html',{'application':application})
    
@login_required
def view_dashboard_job(request,job_id):
    job = get_object_or_404(Job,pk=job_id, owner = request.user)
    return render(request,'accounts/view_dashboard_job.html',{'job':job})
    

##Test Function To Show All Jobs From Other module(Job) this module exist in other Folder(app)
def test(request):
    job_list = Job.objects.all()
    context={'jobs':job_list}
    return render(request,'accounts/test.html',context)
