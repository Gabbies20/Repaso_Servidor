from django.shortcuts import render
from django.db.models import Q,Prefetch
from .models import Proyecto,Tarea,Usuario,Comentario,Etiqueta


# Create your views here.
"""
    1-Desde una página de Inicio debe poder acceder a todas las URLs que se indiquen. 
    Esto no significa que no pueda acceder a algunas URLs desde otros sitios. 
    Pero desde la página de Inicio tengo que poder acceder a un ejemplo de las 
    URLs que se realicen a continuación.    
"""
def index(request):
    return render(request, 'gestion/index.html',{}) 


"""
    2-Crea una URL que muestre una lista de todos los proyectos de la aplicación 
    con sus datos correspondientes.
"""

def listar_proyectos(request):
    
    proyectos = Proyecto.objects.select_related('creador').prefetch_related('usuarios_proyectos_asignados')
    return render(request, "gestion/lista.html", {"proyectos":proyectos})

"""
    3.Crear una URL que muestre todas las tareas que están asociadas a un proyecto, ordenadas por fecha de creación descendente.
"""

def tareas_asociados_a_proyectos(request,id_proyecto):
    proyecto = Proyecto.objects.get(pk=id_proyecto) 
    tarea = Tarea.objects.select_related('creador','proyecto').prefetch_related('usuarios_asignados').filter(proyecto = id_proyecto)
    return render(request,'gestion/url3.html',{'mostrar_tareas': tarea,'proyecto_v':proyecto})
