from django.urls import path
from .views import vistaInicio, detallePost, nuevoPost, actualizarPost, borrarPost, nuevaCategoria, categoria, categoriaLista, vistaMegusta, nuevoComentario, acerca
#from . import views

urlpatterns = [
    #path('', views.inicio, name='inicio'),
    path('', vistaInicio.as_view(), name="inicio"),
    path('detalle/<int:pk>', detallePost.as_view(), name="detalle"),
    path('detalle/nuevo/', nuevoPost.as_view(), name="nuevo"),
    path('detalle/actualizar/<int:pk>', actualizarPost.as_view(), name="actualizar"),
    path('detalle/eliminar/<int:pk>', borrarPost.as_view(), name="borrar"),
    path('categoria/nuevo/', nuevaCategoria.as_view(), name="cnuevo"),
    path('categoria/<str:cate>/', categoria, name="categoria"), #Vamos a acomodar los post por las categorías creadas
    path('listacategoria/', categoriaLista, name="categoriaLista"),
    path('megusta/<int:pk>', vistaMegusta, name="megusta"),
    path('detalle/<int:pk>/nuevoComentario/', nuevoComentario.as_view(), name="nuevoComentario"),
    path('acerca/', acerca, name="acerca"),
    
]
