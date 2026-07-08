from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers1 import delocationse
from rest_framework import status,filters

'''
My name is Abdallah shref
UI/UX Designer
Backend Developer
I Use Django(DRF) in this project
'''

@api_view(['GET','POST'])
def Ivison(request):
    """
    API view to handle GET and POST requests for the delocation model.

    - GET: Retrieve a list of all delocation objects, ordered by primary key.
    - POST: Create a new delocation object with the provided data.

    """

    if request.method == 'GET':
        data = delocation.objects.all().order_by('pk')
        serializer = delocationse(data,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = delocationse(data=request.data)
    if serializer.is_valid():   
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE','PATCH'])
def RestIvison(request,pk):
    """
    This is the API for the detail of each object in the model delocation
    this API has four methods:
        - GET: to get the detail of each object
        - PUT: to update the detail of each object
        - PATCH: to update the detail of each object partially
        - DELETE: to delete the detail of each object
    """
    try:
        data = delocation.objects.get(pk=pk)
    except delocation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = delocation.objects.get(pk=pk)
        serializer = delocationse(data)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = delocationse(data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PATCH':
        serializer = delocationse(data,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
