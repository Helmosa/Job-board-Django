#### Get Data From Model ====> [Json Data]

from rest_framework import serializers
from .models import Job
# Create Serializer 
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

