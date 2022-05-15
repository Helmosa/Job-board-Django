from email.mime import application
from django.db import models
from django.contrib.auth.models import User
#from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from job.models import Job,ApllayJob
# Create your models here.

user_type = (
    ('Job Seeker','JobSeeker'),
    ('Employer','Employer'),
)
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile',on_delete=models.CASCADE)
    User_Type = models.CharField(max_length=30,choices=user_type) 
    #is_employer = models.BooleanField(default=False) #by default the user will register as a jobseeker
    city = models.ForeignKey('City',related_name='user_city', on_delete=models.CASCADE,blank=True,null=True)
    #phone = PhoneNumberField()
    phone = models.CharField(max_length = 15,blank=True,null=True)
    image = models.ImageField(upload_to='profile/',blank=True,null=True)
    company_Name= models.CharField(max_length=60,blank=True,null=True)
    

    def __str__(self):
        return '%s'%(self.user.username)  
class City(models.Model):
    city_name = models.CharField(max_length=50)
    def __str__(self):
        return (self.city_name)    

##  Signals Django (Used To create Profile after create user(register))
def create_profile(sender,**kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)


class NameComapny(models.Model):
    Company_Name = models.CharField(max_length = 60)
    
class ConversationMessage(models.Model):
    application = models.ForeignKey(ApllayJob, related_name='conversationmessages', on_delete=models.CASCADE)
    content = models.TextField()
    sender = models.ForeignKey(User,related_name='sender',on_delete=models.CASCADE)
    reciever = models.ForeignKey(User,related_name='reciever',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']