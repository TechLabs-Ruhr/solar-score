
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.decorators import api_view
import pipeline
import sys
import json
import logging
logger = logging.getLogger(__name__)
from django.shortcuts import render
from django.http import HttpResponse

class UserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    
# Create your views here.

@api_view(['GET'])
def load_testinka(request):
    #  critical logging level so that it really gets displayed in the console
    logger.critical(f"request is {request}")
    logger.critical("DEMO DATA LOADING CALLED")

    res = helperFunction42() # this could be your python solar score precition script

    # here could the chart be inserted as sting like "chart":"<div> .. </div>"
    data = {"message":"test", "data":res} 

    return HttpResponse(json.dumps(data), content_type = "application/json")

@api_view(['GET'])
def load_testinka(request):
    """Backend data provider for Inka's test button."""
    #  critical logging level so that it really gets displayed in the console
    logger.critical(f"request is {request}")
    logger.critical("DEMO DATA LOADING CALLED")

    res = helperFunction42() # this could be your python solar score precition script

    # here could the chart be inserted as sting like "chart":"<div> .. </div>"
    data = {"message":"test", "data":res} 

    return HttpResponse(json.dumps(data), content_type = "application/json")

@api_view(['GET'])
def load_testmarian(request):
    """Backend data provider for Marian's test button."""
    #  critical logging level so that it really gets displayed in the console
    logger.critical(f"request is {request}")
    logger.critical("DEMO DATA LOADING CALLED")

    x,y = helperFunctionPipeline() # this could be your python solar score precition script

    # here could the chart be inserted as sting like "chart":"<div> .. </div>"
    data = {"message":"test", "x":x, "y":y} 

    return HttpResponse(json.dumps(data), content_type = "application/json")

@api_view(['GET'])
def load_testdenise(request):
    """Backend data provider for Denise's test button."""
    #  critical logging level so that it really gets displayed in the console
    logger.critical(f"request is {request}")
    logger.critical("DEMO DATA LOADING CALLED")

    res = helperFunction42() # this could be your python solar score precition script

    # here could the chart be inserted as sting like "chart":"<div> .. </div>"
    data = {"message":"test", "data":res} 

    return HttpResponse(json.dumps(data), content_type = "application/json")

@api_view(['GET'])
def load_testkatharina(request):
    """Backend data provider for Katharina's test button."""
    #  critical logging level so that it really gets displayed in the console
    logger.critical(f"request is {request}")
    logger.critical("DEMO DATA LOADING CALLED")

    # here could the chart be inserted as sting like "chart":"<div> .. </div>"

    data = {"message":"test", "time": [8,10,12,13,14,16,18], "predictiom": [800,2000,3000,4000,3000,2000,1000]} 

    return HttpResponse(json.dumps(data), content_type = "application/json")

@api_view(['GET'])
def load_testprediction(request):
    #  critical logging level so that it really gets displayed in the console
    logger.critical(f"request is {request}")
    logger.critical("DEMO DATA LOADING CALLED")

    # here could the chart be inserted as sting like "chart":"<div> .. </div>"

    data = {"message":"test", "x": [0,1,2,3,4], "y": [1,3,3,7,42]} 

    return HttpResponse(json.dumps(data), content_type = "application/json")


def helperFunctionPipeline():
    """Returns power data over time."""

    x,y = pipeline.run()
    return x,y

def helperFunction42():
    """Returns just the integer '42'."""
    return 42
