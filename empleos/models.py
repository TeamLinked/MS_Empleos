from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
#https://books.agiliq.com/projects/django-orm-cookbook/en/latest/many_to_many.html

class Usuario(models.Model):
    id_usuario = models.CharField(primary_key=True, max_length=50)

class Categoria(models.Model):
    nombre = models.CharField( max_length = 80, primary_key=True)
    class Meta:
        ordering=('nombre',)

class Empleo(models.Model):
    id_ofertante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='Ofertante_Empleo')
    titulo = models.TextField(null=True, blank=True)
    descripcion = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete = models.SET_DEFAULT, default = 'Otra', related_name='Categoria_Empleo')
    fechaPublicacion = models.DateField(auto_now=False, auto_now_add=True, null=True, blank=True)
    fechaVencimiento = models.DateField(null=True, blank=True)
    class Meta:
        ordering=('fechaPublicacion', 'titulo')

class Postulacion(models.Model):
    id_postulante = models.ForeignKey(Usuario, on_delete = models.CASCADE, related_name='Postulante_Empleo')
    id_empleo = models.ForeignKey(Empleo, on_delete = models.CASCADE, related_name='Empleo_a_postular')
    fechaAplicacion =  models.DateField(auto_now=False, auto_now_add=True, null=True, blank=True)
    class Meta:
        ordering=('fechaAplicacion',)



