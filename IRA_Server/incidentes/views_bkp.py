from django.shortcuts import render
from .models import Incidentes
from django.db import connection
from .form import FormNuevoIncidente
import datetime



#VISTA PARA CREACIÓN DE NUEVO INCIDENTE

def vista_NuevoIncidente(request, *args, **kwargs):

    
    ###############################
    #REGISTROS DE LA TABLA ORIGEN
    ###############################
    cursorOrigen=connection.cursor()
    cursorOrigen.execute('call GetOrigenes()')
    resOrigen=cursorOrigen.fetchall()

    #########################################
    #REGISTROS DE LA TABLA TIPOSINCIDENTES
    #########################################
    cursorTipo=connection.cursor()
    cursorTipo.execute('call GetTiposIncidentes()')
    resTipos=cursorTipo.fetchall()

    #########################################
    #REGISTROS DE LA TABLA ETAPAS
    #########################################
    cursorEtapa=connection.cursor()
    cursorEtapa.execute('call GetEtapas()')
    resEtapas=cursorEtapa.fetchall()

    #########################################
    #REGISTROS DE LA TABLA ACTIVOS
    #########################################
    cursorActivo=connection.cursor()
    cursorActivo.execute('call GetActivos()')
    resActivos=cursorActivo.fetchall()

    #########################################
    #REGISTROS DE LA TABLA IMPACTOS
    #########################################
    cursorImpacto=connection.cursor()
    cursorImpacto.execute('call GetImpactos()')
    resImpactos=cursorImpacto.fetchall()

    #########################################
    #REGISTROS DE LA TABLA URGENCIAS
    #########################################
    cursorUrgencia=connection.cursor()
    cursorUrgencia.execute('call GetUrgencias()')
    resUrgencias=cursorUrgencia.fetchall()

    #########################################
    #REGISTROS DE LA TABLA AMBIENTES
    #########################################
    cursorAmbiente=connection.cursor()
    cursorAmbiente.execute('call GetAmbientes()')
    resAmbientes=cursorAmbiente.fetchall()

    #########################################
    #REGISTROS DE LA TABLA UBICACIONES
    #########################################
    cursorUbicacion=connection.cursor()
    cursorUbicacion.execute('call GetUbicaciones()')
    resUbicaciones=cursorUbicacion.fetchall()

    #########################################
    #REGISTROS DE LA TABLA SERVICIOS
    #########################################
    cursorServicios=connection.cursor()
    cursorServicios.execute('call GetServicios()')
    resServicios=cursorServicios.fetchall()


    return render(request, "nuevo_incidente.html", {'origen':resOrigen, 'tipoincidente':resTipos, 'etapa':resEtapas, 
                            'activo':resActivos,'impacto':resImpactos, 'urgencia': resUrgencias, 
                            'ambiente':resAmbientes, 'ubicacion':resUbicaciones, 'servicio':resServicios})

    

    
def vista_IncidenteCreado(request, *args, **kwargs):
    return render(request, "incidente_creado.html", {})
  

def Form_Test(request, *args, **kwargs):
    if request.method == 'POST':
        formito = FormNuevoIncidente(request.POST)

        if formito.is_valid():
            print("ES VALIDO: ")
            etapa=formito.cleaned_data['etapa']
            print(etapa)
            return render(request, "test.html", {'formito':formito})

        else:
            print("NO ES VALIDO: ")
            return render(request, "test.html", {'formito':formito})

    formito = FormNuevoIncidente()

    return render(request, "test.html", {'formito':formito})