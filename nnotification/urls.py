# from django.urls import include,path 
# from .views import notification


# app_name = 'nnotification'

# urlpatterns = [
    
#     path('',notification,name='notification'),

# ]

from django.urls import include,path 
from . import views

app_name = 'nnotification'

urlpatterns = [
    path('',views.notification,name='notification'),
]
