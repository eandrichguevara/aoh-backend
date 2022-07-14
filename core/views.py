from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated

from core.models import Producto

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def lista_productos(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        #serializer = ModelSerializer(model, many=True)
        #return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        #serializer = ModelSerializer(data=data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #else:
            #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
