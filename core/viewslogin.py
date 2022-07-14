import os

from django.shortcuts import render
import jwt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from core.models import Cliente, Producto, Usuario
from core.serializers import ProductoSerializer

from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token


@csrf_exempt
@api_view(['POST'])
def signinCliente(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        username = data['username']
        password = data['password']
        try:
            user = Cliente.objects.get(username=username)
        except Cliente.DoesNotExist:
            return Response("El usuario no existe")
        pass_valido = check_password(password, user.password)
        if not pass_valido:
            return Response("Contraseña Incorrecta")

        return Response({"success": True})


@csrf_exempt
@api_view(['POST'])
def signupCliente(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        username = data['username']
        password = data['password']
        try:
            user = Cliente.save()
        except:
            return Response({"success": False})

        return Response({"success": True})

@csrf_exempt
@api_view(['POST'])
def signinUsuario(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        username = data['username']
        password = data['password']
        try:
            user = Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            return Response("El usuario no existe")
        pass_valido = check_password(password, user.password)
        if not pass_valido:
            return Response("Contraseña Incorrecta")

        return Response({"success": True})


@csrf_exempt
@api_view(['POST'])
def signupUsuario(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        username = data['username']
        password = data['password']
        try:
            user = Usuario.save()
        except:
            return Response({"success": False})

        return Response({"success": True})
