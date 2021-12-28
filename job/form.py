from django import forms
from django.db.models import fields
from .models import ApllayJob, Job
from ckeditor.widgets import CKEditorWidget
class ApplyForm(forms.ModelForm):
    
    class Meta:
        model = ApllayJob
        fields = ['name','email','website','cv','coverLetter']
        

class add_job_form(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('slug','owner')