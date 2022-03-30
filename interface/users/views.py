from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
import json
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.decorators import api_view
import logging
logger = logging.getLogger(__name__)


class UserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    
# Create your views here.

@api_view(['GET'])
def load_demo_data(request):
    #  critical logging level so that it really gets displayed in the console
    logger.critical(f"request is {request}")
    logger.critical("DEMO DATA LOADING CALLED")

    res = helperFuntion() # this could be your python solar score precition script

    # here could the chart be inserted as sting like "chart":"<div> .. </div>"
    data = {"message":"test", "data":res} 

    return HttpResponse(json.dumps(data), content_type = "application/json")

def helperFuntion():
    return 42