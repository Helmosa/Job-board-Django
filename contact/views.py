from django.shortcuts import render
from .models import ContactUS
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def send_message(request):
    mycontact= ContactUS.objects.first()
    
    if request.method == 'POST': 
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST['email']
        name =request.POST['name']
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER, #elglladcybersec@gmail.com
            [email],
            fail_silently=False,
)
    return render(request,'contact/contact.html',{'mycontact':mycontact})