from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('listar',views.listar_proyectos,name='lista'),
    path('tareas-asociadas/<int:id_proyecto>',views.tareas_asociados_a_proyectos,name='tareas_asociadas')
]

