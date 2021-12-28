import django_filters
from .models import Job
class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = ['category','title','job_type','description','experience']
        exclude = ['img','owner','slug','vacancy','published_at','salary']