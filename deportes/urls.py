from django.conf.urls import url
from . import views


urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^pelicula/listar/$', views.listar_deportista, name='listar_deportista'),
    url(r'^pelicula/nueva/$', views.pelicula_nueva, name='pelicula_nueva'),
    url(r'^deportista/(?P<pk>\d+)/remove/$',views.borrar_deportista, name='borrar_deportista'),
    url(r'^editar_deportista/(?P<pk>[0-9]+)/$', views.editar_deportista, name='editar_deportista'),
    url(r'^pelicula/listard/$', views.deporte_listar, name='deporte_listar'),
    url(r'^deporte/creardeporte/$', views.crear_deporte, name='crear_deporte'),
    url(r'^deporte/(?P<pk>\d+)/remove/$',views.borrar_deporte, name='borrar_deporte'),
    url(r'^deporte/(?P<pk>[0-9]+)/editar/$', views.editar_deporte, name='editar_deporte'),
    ]
