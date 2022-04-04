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
    logger.critical(f"request is {request} with {request.user.id}")
    logger.critical("'load_testmarian' called")

    try:
        user:CustomUser = CustomUser.objects.get(pk=request.user.id)

        print(float(user.pv))

        x,y = pipeline.run(user.address, float(user.pv))
        data = {"message":"test", "x":x, "y":y} 
        return HttpResponse(json.dumps(data, default=str), content_type = "application/json")

    except CustomUser.DoesNotExist:
        user = None
        logger.critical("User does not exist")
        return HttpResponseNotFound("User does not exist")

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
    logger.critical(f"request is {request} with {request.user.id}")
    logger.critical("DEMO DATA LOADING CALLED")

    # here could the chart be inserted as sting like "chart":"<div> .. </div>"

    #data = {"time": [8,10,12,13,14,16,18], "prediction": [800,2000,3000,4000,3000,2000,1000]} 
    user:CustomUser = CustomUser.objects.get(pk=request.user.id)
    x,y = pipeline.run(user.address, float(user.pv))
    data=[]
    for i, j in zip(x, y):
        dict={"time":i.strftime("%H:%M"),"prediction":"{} kW".format(str(round(j,2)))}
        data.append(dict)
        print(data)
        logger.critical(data)

#     data= [
#     {"time": "8:00", "prediction": "890 W"}, 
#     {"time": "10:00", "prediction": "1000 W"}, 
#     {"time": "12:00", "prediction": "5000 W"}, 
#     {"time": "14:00", "prediction": "5800 W"}, 
#     {"time": "16:00", "prediction": "4800 W"},
#     {"time": "18:00", "prediction": "3800 W"}
#   ]

    return HttpResponse(json.dumps(data,default=str), content_type = "application/json")

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
