from django.contrib import admin
from .models import Job , Category,ApllayJob

# Register your models here.

#Custom Admin 
class Filter(admin.ModelAdmin):
    list_filter = ['category']
    list_display = ['title','job_type','published_at','experience','vacancy']
    search_fields = ['title','description']


admin.site.register(Job,Filter)
admin.site.register(Category)
admin.site.register(ApllayJob)
