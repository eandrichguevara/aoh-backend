from django.db import models

#modelo para el cliente
class Cliente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.id

#modelos para el usuario
class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.id

# modelo para el producto
class Producto(models.Model):
    sku = models.CharField(max_length=15, primary_key=True, verbose_name='SKU')
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=1000, null=True, blank=True)
    precio = models.IntegerField()
    stock = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.sku

# modelo para el descuent9
class Descuento (models.Model):
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.id

# modelo para el despacho
class Despacho (models.Model):
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.id

# modelo para la venta
class Venta(models.Model):
    id = models.IntegerField(primary_key=True)
    total = models.IntegerField()
    descuento = models.ForeignKey(Descuento, on_delete=models.CASCADE)
    despacho = models.ForeignKey(Despacho, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class DetalleVenta(models.Model):
    id = models.IntegerField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)

    def __str__(self):
        return self.id