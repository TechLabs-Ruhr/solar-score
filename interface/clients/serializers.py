from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    abstract=True
    class Meta:
        abstract = True
        model = Client
        fields = ('id', 'location', 'p_max')