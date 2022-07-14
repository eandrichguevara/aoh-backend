from rest_framework import serializers
from core.models import Producto, Venta

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['sku', 'nombre', 'descripcion', 'precio', 'stock', 'usuario']

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ['id', 'total', 'descuento', 'despacho', 'cliente']