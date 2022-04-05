from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from .models import CustomUser
from .serializers import UserSerializer

from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication
from rest_framework import viewsets

import numpy as np
import pipeline
import sys
import json
import logging
logger = logging.getLogger(__name__)

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import datetime

class UserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    
# Create your views here.

@api_view(['GET'])
def load_powerchart(request):
    """Starts calculation pipeline and sends data to frontend for visualizing."""
    #  critical logging level so that it really gets displayed in the console
    logger.critical(f"request is {request} with {request.user.id}")
    logger.critical("'load_powerchart' called")

    try:
        user:CustomUser = CustomUser.objects.get(pk=request.user.id)

        x,y = pipeline.run(user.address, float(user.pv))
        data = {"message":"test", "x":x, "y":y} 
        return HttpResponse(json.dumps(data, default=str), content_type = "application/json")

    except CustomUser.DoesNotExist:
        return HttpResponseNotFound("User does not exist")

@api_view(['GET'])
def load_powertable(request):
    """Starts calculation pipeline and sends data to frontend for listing."""
    #  critical logging level so that it really gets displayed in the console
    logger.critical(f"request is {request} with {request.user.id}")
    logger.critical("'load_powertable' called")

    try:
        user:CustomUser = CustomUser.objects.get(pk=request.user.id)

        x,y = pipeline.run(user.address, float(user.pv))
        data=[]
        for i, j in zip(x, y):
            dict={"time":i.strftime("%H:%M"),"prediction":"{} kW".format(str(round(j,2)))}
            data.append(dict)

        return HttpResponse(json.dumps(data, default=str), content_type = "application/json")

    except CustomUser.DoesNotExist:
        return HttpResponseNotFound("User does not exist")

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
def load_testprediction(request):
    #  critical logging level so that it really gets displayed in the console
    logger.critical(f"request is {request} with {request.user.id}")
    logger.critical("DEMO DATA LOADING CALLED")

    # here could the chart be inserted as sting like "chart":"<div> .. </div>"

    x = np.linspace(0, 20*np.pi, 240).tolist()
    y = (np.sin(x)+1).tolist()

    data = {"message":"test", "x": x, "y": y} 

    return HttpResponse(json.dumps(data), content_type = "application/json")


def helperFunction42():
    """Returns just the integer '42'."""
    return 42
