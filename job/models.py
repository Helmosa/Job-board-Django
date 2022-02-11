from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField, TextField
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

# Customize Image Upload
def image_upload(instance,filename):
    imagename , extension = filename.split('.')
    return "jobs/%s/%s.%s"%(instance.id,instance.id,extension)

class Job(models.Model):            #table
    owner = models.ForeignKey(User,related_name='job_owner',on_delete=CASCADE)   # column                                     #column
    title = models.CharField(max_length=40) 
    location = models.CharField(max_length=30)
    job_type = models.CharField(max_length=15,choices=JOB_TYPE) 
    description = RichTextField()
    #description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now_add=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    category = models.ForeignKey('Category',on_delete=CASCADE)
    img = models.ImageField(upload_to=image_upload,blank=True,null=True)
    slug = models.SlugField(blank=True,null=True)
    
    
    #Slug Function
    def save(self,*args, **kwargs):
        ##logic
        self.slug = slugify(self.title)
        super(Job,self).save(*args,**kwargs)
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    
class ApllayJob(models.Model):
    job = models.ForeignKey(Job,related_name='applications',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = EmailField(max_length=100)
    portfolio_link = models.URLField(blank=True,null=True)
    cv = models.FileField(upload_to='apply_job/')
    coverLetter= TextField(max_length=500)
    created_by = models.ForeignKey(User,related_name='applications',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name