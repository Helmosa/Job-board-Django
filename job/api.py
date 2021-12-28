#### views in api [josn data]

from django.contrib.auth import decorators
from django.http import response
from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def job_list_api(request):
    all_jobs = Job.objects.all()  # Normal Data
    Data = JobSerializer(all_jobs, many=True).data  # Json Data By Serializers Class
    return Response({'data':Data})
@api_view(['GET'])
def job_detail_api(request,id):
    job_dtail = Job.objects.get(id=id) # normal Data
    Data = JobSerializer(job_dtail).data  # Json Data By Serializers Class
    return Response({'data':Data})

class JobListApi(generics.ListCreateAPIView):   # generics Views [api/v2]
    model = Job
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    
class JobDetails(generics.RetrieveUpdateDestroyAPIView): #[DELETE,PUT,Retrieve] generics Views [api/v2/id]
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    lookup_field = 'id'