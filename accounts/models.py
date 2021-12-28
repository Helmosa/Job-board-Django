from django.db import models
from django.contrib.auth.models import User
#from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    city = models.ForeignKey('City',related_name='user_city', on_delete=models.CASCADE,blank=True,null=True)
    #phone = PhoneNumberField()
    phone = models.CharField(max_length = 15,blank=True,null=True)
    image = models.ImageField(upload_to='profile/')
    
    def __str__(self):
        return '%s'%(self.user.username)
    
class City(models.Model):
    city_name = models.CharField(max_length=50)
    def __str__(self):
        return (self.city_name)    

##  Signals Django To add New Users In DB
def create_profile(sender,**kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)