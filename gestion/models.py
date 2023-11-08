
from django.conf import settings
from django.utils import timezone
from django.db import models



# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    correo_electronico = models.CharField(max_length=100,unique=True)
    contraseña = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(default=timezone.now)
    

class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    duracion_estimada = models.FloatField()
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_finalizacion = models.TimeField(default=timezone.now)
    #Relacion con Proyectos Asignados
    usuarios_proyectos_asignados = models.ManyToManyField(Usuario,related_name='colaboradores_proyecto')
    #Relacion con usuario:un proyecto tiene un usuario que lo crea y lo administra.
    creador = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='creador_proyecto')
    
    
class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    ESTADOS=[('PE','Pendiente'),('PR','Progreso'),('Co','Completada')]
    estado=models.CharField(max_length=2,choices=ESTADOS)
    completada = models.BooleanField()
    fecha_creacion = models.DateField(default=timezone.now)
    hora_vencimiento = models.TimeField(default=timezone.now)
    #Relacion con usuario: muchas tareas pueden ser creadas por un usuario:ManytoOne es ForeignKey
    creador = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name="creador_tarea")
    #Una tarea puede tener asignado uno o más usuarios y un usuario puede estar en varias tareas.
    usuarios_asignados = models.ManyToManyField(Usuario,through='AsignacionTarea',related_name='colaboradores_tarea')
    #Relacion con Proyecto:Un proyecto tiene varias tareas creadas.
    proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    
class Etiqueta(models.Model):
    nombre = models.CharField(unique=True,max_length=50)
    #Relacion con etiqueta:Una tarea puede tener varias etiquetas. Y una etiqueta puede estar asignada a varias tareas.
    etiquetas_asociadas = models.ManyToManyField(Tarea)
    
    
class AsignacionTarea(models.Model):
    observaciones = models.TextField()
    fecha_asignacion = models.DateTimeField(default=timezone.now)
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    tarea=models.ForeignKey(Tarea,on_delete=models.CASCADE)


class Comentario(models.Model):
    contenido = models.TextField()
    fecha_de_comentario = models.DateTimeField(default=timezone.now)
    """
        Relación con Usuario (Autor): Cada comentario tiene un autor (usuario). 
    """
    autor=models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name="comentarios_creador")
    
    """
        Relación con Tarea: Cada comentario está asociado a una tarea. 
    """
    tarea=models.ForeignKey(Tarea,on_delete=models.CASCADE,related_name="comentarios_tarea")