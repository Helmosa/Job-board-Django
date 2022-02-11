from django.db.models.query import QuerySet
from django.http import request
from django.shortcuts import render,redirect
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm,add_job_form
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JobFilter
from django.contrib import messages
# Create your views here.



## Home Page
def index(request):
    job_list = Job.objects.all()
    context={'jobs':job_list}
    return render(request,'job/index.html',context)
    


## All Jobs 
def job_list(request):
    job_list = Job.objects.all()
    
    ##Filter
    myfilter = JobFilter(request.GET,queryset=job_list)
    job_list = myfilter.qs
    
    # Adding paginator  
    paginator = Paginator(job_list, 3) # Show 3 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'jobs' : page_obj,       # jobs in Template Name
        'myfilter':myfilter,
    }

    return render(request,'job/job_list.html',context)

@login_required
## Jobs Details
def job_details(request, slug):
    job_details = Job.objects.get(slug=slug)
    # Aplly Form
    if request.method=='POST':
        form = ApplyForm(request.POST, request.FILES) # request Files ==> CV 
        if form.is_valid():
            myform = form.save(commit=False) #Don't Save in DB
            myform.job = job_details #job ==> دا ال field بتاع الوظيفه 
            myform.created_by = request.user # دا عشان نجيب اليوزر الي ملي الابليكشن عشان يستغل
            myform.save() #Save in DB
            messages.success(request, 'Your CV Has Been Sended we will review your CV And Back To You If It Approaved! Pleas Go To Dashboard Page')
            return redirect(reverse('jobs:done_job'))
            
    else:
        form = ApplyForm()


    context={
        'job': job_details,
        'form': form
    }
    return render(request,'job/job_details.html',context)

#Done Sending Request Job
@login_required
def done_job(request):
    return render(request,'job/done_job.html')


# Add Job
@login_required
def add_job(request):
    if request.method=='POST':
        form = add_job_form(request.POST,request.FILES)
        if form.is_valid():            
            myform= form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = add_job_form() 
    
    context={
        'form': form,   
    }
    
    return render(request,'job/add_job.html',context)
