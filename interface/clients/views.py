from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes
from rest_framework import status
from rest_framework.renderers import BrowsableAPIRenderer
import logging
logger = logging.getLogger(__name__)

from .models import Client
from .serializers import ClientSerializer

@api_view(['GET', 'POST'])
def clients_list(request):
    logger.critical(f"Request is {request}")
    logger.critical("'clients_list' called")
    if request.method == 'GET':
        data = Client.objects.all()
        serializer = ClientSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def clients_detail(request, pk):
    logger.critical(f"Request is {request} with {pk}")
    logger.critical("'clients_detail' called")

    try:
        client:Client = Client.objects.get(pk=pk)
        print(client.location)

    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientSerializer(client, context={'request': request}, many=True)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ClientSerializer(client, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
