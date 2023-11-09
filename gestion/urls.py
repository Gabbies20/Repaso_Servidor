from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('listar',views.listar_proyectos,name='lista'),
    path('tareas-asociadas/<int:id_proyecto>',views.tareas_asociados_a_proyectos,name='tareas_asociadas'),
    path('usuarios-tareas/<int:id_tarea>',views.usuarios_asociados_a_tareas,name='usuarios_tareas')
]

