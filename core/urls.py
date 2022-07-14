from django.urls import path
from core.views import productos
from core.viewslogin import signinCliente, signupCliente

urlpatterns = [
    path('productos', productos, name="productos"),
    path('clientes', signinCliente, name="productos"),
]