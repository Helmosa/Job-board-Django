from django.urls import include,path 
from . import views
from . import api


app_name = 'job'

urlpatterns = [
    path('',views.index,name='index'),
    path('jobs/',views.job_list,name='job_list'),
    path('jobs/add',views.add_job,name='add_job'),
    path('jobs/add/done/',views.done_job,name='done_job'),
    path('<str:slug>',views.job_details,name='job_detail'),

    
    #api urls
    path('api/jobs',api.job_list_api,name='job_list _api'),
    path('api/jobs/<int:id>',api.job_detail_api,name='job_detail_api'),

    # Class Based Views
    path('api/v2/jobs',api.JobListApi.as_view(),name='job_detail_api'),
    path('api/v2/jobs/<int:id>',api.JobDetails.as_view(),name='job_detail_api'),

]
