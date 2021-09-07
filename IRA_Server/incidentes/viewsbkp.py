from django.shortcuts import render
from .models import Incidentes, FormIncidente
from django.db import connection
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

    if request.method=="POST":
        incidente=Incidentes()

        inctest=FormIncidente(request.POST)
        """
        incidente.id_origen=int(request.POST.get('origen'))
        incidente.id_tipo=int(request.POST.get('tipoincidente'))
        incidente.desc_inc=request.POST.get('descripcion')
        incidente.id_etapa=int(request.POST.get('etapa'))
        incidente.cli_afectados=int(request.POST.get('clientes'))
        incidente.prov_involucrado=int(request.POST.get('proveedores'))
        incidente.act_afectados=int(request.POST.get('activos'))

        ambiente=request.POST.getlist('ambiente')
        for i in ambiente:
            print(int(i))

        ubicacion=request.POST.getlist('ubicacion')
        for i in ubicacion:
            print(int(i))

        servicio=request.POST.getlist('servicio')
        for i in servicio:
            print(int(i))

        incidente.id_impacto=int(request.POST.get('impacto'))
        incidente.id_urgencia=int(request.POST.get('urgencia'))

 
        if incidente.id_etapa == 1:
            incidente.id_estado = 1
        elif incidente.id_etapa == 6:
            incidente.id_estado = 3
        elif incidente.id_etapa == 7:
            incidente.id_estado = 4
        else:
            incidente.id_estado = 2
        
        incidente.cont_comentarios=0
        incidente.cont_documentos=0
        incidente.ts_inc=datetime.datetime.now()
        incidente.id_severidad=1

        print("===============================================")
        print("===============================================")
        print("===============================================")

        print("cli_afectados")
        print(incidente.cli_afectados)
        print("id_origen")
        print(incidente.id_origen)
        print("id_tipo")
        print(incidente.id_tipo)
        print("desc_inc")
        print(incidente.desc_inc)
        print("id_etapa")
        print(incidente.id_etapa)
        print("id_estado")
        print(incidente.id_estado)
        print("act_afectados")
        print(incidente.act_afectados)
        print("prov_involucrado")
        print(incidente.prov_involucrado)
        print("id_urgencia")
        print(incidente.id_urgencia)
        print("id_impacto")
        print(incidente.id_impacto)
        print("incidente.cont_comentarios")
        print(incidente.cont_documentos)
        print("incidente.cont_documentos")
        print(incidente.cont_comentarios)
        print("incidente.ts_inc")
        print(incidente.ts_inc)
        print("incidente.id_severidad")
        print(incidente.id_severidad)


        print("===============================================")
        print("===============================================")
        print("===============================================")

        inctest.id_origen=int(request.POST.get('origen'))
        inctest.id_tipo=int(request.POST.get('tipoincidente'))
        inctest.desc_inc=request.POST.get('descripcion')
        inctest.id_etapa=int(request.POST.get('etapa'))
        inctest.cli_afectados=int(request.POST.get('clientes'))
        inctest.prov_involucrado=int(request.POST.get('proveedores'))
        inctest.act_afectados=int(request.POST.get('activos'))
        inctest.id_impacto=int(request.POST.get('impacto'))
        inctest.id_urgencia=int(request.POST.get('urgencia'))

 
        if inctest.id_etapa == 1:
            inctest.id_estado = 1
        elif inctest.id_etapa == 6:
            inctest.id_estado = 3
        elif inctest.id_etapa == 7:
            inctest.id_estado = 4
        else:
            inctest.id_estado = 2

        inctest.id_severidad=1

        print("cli_afectados")
        print(inctest.cli_afectados)
        print("id_origen")
        print(inctest.id_origen)
        print("id_tipo")
        print(inctest.id_tipo)
        print("desc_inc")
        print(inctest.desc_inc)
        print("id_etapa")
        print(inctest.id_etapa)
        print("id_estado")
        print(inctest.id_estado)
        print("act_afectados")
        print(inctest.act_afectados)
        print("prov_involucrado")
        print(inctest.prov_involucrado)
        print("id_urgencia")
        print(inctest.id_urgencia)
        print("id_impacto")
        print(inctest.id_impacto)
        print("inctest.id_severidad")
        print(inctest.id_severidad)


        print("===============================================")
        print("===============================================")
        print("===============================================")
        """

        if inctest.is_valid():
            print ('FUNCINO Y EL MODELO ES VALIDO!!')
            return render(request, "incidente_creado.html", {'inctest':inctest})
        else:
            print ('NO FUNCINO!!!')
            print (inctest.errors)            

            return render(request, "incidente_creado.html", {'inctest':inctest})
    