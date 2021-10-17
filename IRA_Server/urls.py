from django.contrib import admin
from django.urls import path
from .incidentes.vistas.login import *
from .incidentes.vistas.dashboard import *
from .incidentes.vistas.detalle_incidente import *
from .incidentes.vistas.nuevo_incidente import *
from .incidentes.vistas.reportes import *
from .incidentes.vistas.perfil_usuario import *
from .incidentes.vistas.incidentes_activos import *
from .incidentes.vistas.panel_administracion import *
from .incidentes.vistas.detalle_usuario import *
from .incidentes.vistas.nuevo_usuario import *
from .incidentes.vistas.eliminar_usuario import *

urlpatterns = [
    path('admin/', admin.site.urls),

    #URL DASHBOARD PRINCIPAL
    path('Dashboard/', cargar_dashboard, name='dashboard'),

    #INICIO Y CIERRE DE SESION
    path('', iniciar_sesion, name='home'), #SI LA SESION ESTA INICIADA REDIRIGE AL DASHBOARD
    path('Login/', iniciar_sesion, name='login'),
    path('Logout/', cerrar_sesion, name='logout'),

    #URL PARA CARGA DE INCIDENTE NUEVO
    path('NuevoIncidente/', crear_incidente, name='nuevo'),

    #URL PARA INCIDENTES ACTIVOS
    path('IncidentesActivos/', cargar_incidentes_activos, name='activos'),

    #URL PARA DETALLE DE INCIDENTE
    path('DetalleIncidente/', cargar_incidente, name='detalle'),

    #URL PARA PERFIL USUARIO
    path('PerfilUsuario/', cargar_perfil, name='perfil'),

    #URL PARA REPORTERIA
    path('Reportes/', cargar_reportes, name='reportes'),

    #URL PARA INCIDENTE NO ENCONTRADO
    path('NoEncontrado/', no_encontrado, name='noencontrado'),

    #URL PARA EL PANEL DE ADMINISTRACIÓN
    path('Administracion/', cargar_admin, name='administracion'),

    #URL PARA VER EL DETALLE DE UN USUARIO
    path('DetalleUsuario/', cargar_usuario, name='detalleusuario'),

    #URL PARA USUARIO NO ENCONTRADO
    path('UsuarioInvalido/', usuario_invalido, name='usuarioinvalido'),

    #URL PARA USUARIO NUEVO
    path('CrearUsuario/', crear_usuario, name='crearusuario'),

    #URL PARA USUARIO NUEVO
    path('/EliminarUsuario', eliminar_usuario, name='eliminarusuario'),
    

]
