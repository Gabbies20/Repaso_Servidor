from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    correo_electronico = models.CharField(max_length=100,unique=True)
    contraseña = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(default=timezone.now)
    
    


class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    ESTADOS=[('PE','Pendiente'),('PR','Progreso'),('Co','Completada')]
    estado=models.CharField(max_length=2,choices=ESTADOS)
    completada = models.BooleanField()
    fecha_creacion = models.DateField(default=timezone.now)
    hora_vencimiento = models.TimeField(default=timezone.now)
    



class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    duracion_estimada = models.FloatField()
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_finalizacion = models.TimeField(default=timezone.now)
    
    
    
class Etiqueta(models.Model):
    nombre = models.CharField(unique=True,max_length=50)
    
    
class AsignacionTarea(models.Model):
    observaciones = models.TextField()
    fecha_asignacion = models.DateTimeField(default=timezone.now)
    


class Comentario(models.Model):
    contenido = models.TextField()
    fecha_de_comentario = models.DateTimeField(default=timezone.now)