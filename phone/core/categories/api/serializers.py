from ..models import phone
from rest_framework import serializers
class phoneserializer(serializers.ModelSerializer):
    class Meta:
        model= phone
        fields= '__all__'