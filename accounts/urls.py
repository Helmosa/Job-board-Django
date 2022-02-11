from django.urls import include,path 
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/',views.signup,name='register'),
    path('signup_CO/',views.signupCo,name='register_CO'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit',views.profile_edit,name='profile_edit'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard/<int:job_id>',views.view_dashboard_job,name='view_dashboard_job'),
    path('application/<int:application_id>',views.view_application,name='view_application'),
    path('test/',views.test,name='test'),
    
]
