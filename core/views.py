import os

from django.shortcuts import render
import jwt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from core.models import Producto, Venta
from core.serializers import ProductoSerializer, VentaSerializer


@csrf_exempt
@api_view(['GET'])
def productos(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)



@csrf_exempt
@api_view(['GET'])
def ventas(request):
    if request.method == 'GET':
        ventas = Venta.objects.all()
        serializer = VentaSerializer(ventas, many=True)
        return Response(serializer.data)



@csrf_exempt
@api_view(['GET', 'POST'])
def venta(request, id):
    if request.method == 'GET':
        
        venta = Venta.objects.get(id = id)
        serializer = VentaSerializer(venta, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        
        data = JSONParser().parse(request)
        
        total = data['total']
        descuento = data['descuento']

        venta = Venta()
        venta.total
        
        return Response(serializer.data)