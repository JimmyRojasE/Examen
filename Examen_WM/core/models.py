from django.db import models

# Create your models here.
class Categoria(models.Model):
   nombre_cat=models.CharField(max_length=50)
   def __str__(self):
        return self.nombre_cat

class Estado_Producto(models.Model):
    nombre_estado_producto=models.CharField(max_length=20)
    def __str__(self):
        return self.nombre_estado_producto

class Producto(models.Model):
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    precio_promocion = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.CharField(max_length=250)
    id_categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_estado_producto=models.ForeignKey(Estado_Producto, on_delete=models.CASCADE)
    def __str__(self):
        return self.descripcion