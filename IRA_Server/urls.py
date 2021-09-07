"""IRA_Server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from .incidentes.vistas.login import *
from .incidentes.vistas.dashboard import *
from .incidentes.vistas.detalle_incidente import *
from .incidentes.vistas.nuevo_incidente import *
from .incidentes.vistas.reportes import *
from .incidentes.vistas.perfil_usuario import *
from .incidentes.vistas.incidentes_activos import *

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

]
