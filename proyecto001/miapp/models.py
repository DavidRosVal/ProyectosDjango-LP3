from django.db import models

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    imagen = models.ImageField(default='null')
    publicado = models.BooleanField()
    creado = models.DateTimeField(auto_now_add=True) # auto_now_add me permitirá registrar la fecha cuando cree el registro
    actualizado = models.DateTimeField(auto_now=True) # auto_now me permitirá registrar la fecha cuando se modifique el registro

class Categoria(models.Model):
    nombre = models.CharField(max_length=110)
    descripcion = models.CharField(max_length=250)
    creado = models.DateField() # DateField() para guardar la fecha manualmente

