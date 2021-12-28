from django.db import models

# Create your models here.
class ContactUS(models.Model):
    place= models.CharField(max_length = 150)
    phone= models.CharField(max_length=15)
    email = models.EmailField(max_length=254)


    def __str__(self):
        return self.email
