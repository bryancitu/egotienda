from django.db import models
from autoslug import AutoSlugField
from usuarios.models import Usuario
# Create your models here.

class Categoria(models.Model):

    titulo = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='titulo',unique=True)

    def __str__(self):                                                                               
        return self.titulo

class Subcategoria(models.Model):

    categoria = models.ForeignKey(Categoria, related_name='categoria', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='titulo',unique=True)

    def __str__(self):                                                                               
        return self.titulo

class Producto(models.Model):

    categoria = models.ForeignKey(Categoria, related_name='categoria_producto', on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, related_name='subcategoria_producto', on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, related_name='subcategoria_producto', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=1000)
    precio = models.DecimalField(max_digits=12,decimal_places=0)
    imagen = models.ImageField(upload_to='producto-%Y-%m')
    slug = AutoSlugField(populate_from='titulo',unique=True)

    def __str__(self):                                                                               
        return self.titulo