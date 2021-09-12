from django.db import models
from django.forms import ModelForm
from django.db import connection

class DashboardSeveridades(models.Model):

    ###############################
    # 1- CARGA SEVERIDAD BAJA
    ###############################

    cursorBaja=connection.cursor()
    cursorBaja.execute('call GetIncidentesBaja()')
    resBaja=cursorBaja.fetchall()
    contBaja=resBaja[0][0]
    connection.close()


    ############################### ###
    # 2- CARGA SEVERIDAD MEDIA
    ###############################

    cursorMedia=connection.cursor()
    cursorMedia.execute('call GetIncidentesMedia()')
    resMedia=cursorMedia.fetchall()
    contMedia=resMedia[0][0]
    connection.close()


    ###############################
    # 3- CARGA SEVERIDAD ALTA
    ###############################

    cursorAlta=connection.cursor()
    cursorAlta.execute('call GetIncidentesAlta()')
    resAlta=cursorAlta.fetchall()
    contAlta=resAlta[0][0]
    connection.close()


class DashboardTop(models.Model):
    ###############################
    # 1- TOP 5 SERVICIOS
    ###############################

    cursorServicios=connection.cursor()
    cursorServicios.execute('call GetTopServicio()')
    resServicios=cursorServicios.fetchall()
    contServicio=[]
    for o in resServicios:
        contServicio.append([o[0],o[1],o[2]])
        print(o[0],o[1],o[2])
    connection.close()

    ###############################
    # 2- TOP 5 UBICACIONES
    ###############################

    cursorUbicacion=connection.cursor()
    cursorUbicacion.execute('call GetTopUbicacion()')
    resUbicacion=cursorUbicacion.fetchall()
    contUbicacion=[]
    for o in resUbicacion:
        contUbicacion.append([o[0],o[1],o[2]])
    connection.close()

    ###############################
    # 3- TOP 5 AMBIENTES
    ###############################

    cursorAmbientes=connection.cursor()
    cursorAmbientes.execute('call GetTopAmbiente()')
    resAmbientes=cursorAmbientes.fetchall()
    contAmbiente=[]
    for o in resAmbientes:
        contAmbiente.append([o[0],o[1],o[2]])
    connection.close()

    ###############################
    # 4- TOP 5 TIPOS DE INCIDENTES
    ###############################

    cursorTipos=connection.cursor()
    cursorTipos.execute('call GetTopTipoIncidente()')
    resTipos=cursorTipos.fetchall()
    contTipo=[]
    for o in resTipos:
        contTipo.append([o[0],o[1],o[2]])
    connection.close()

    ###############################
    # 5- TOP 5 ORIGENES DE INCIDENTES
    ###############################

    cursorOrigenes=connection.cursor()
    cursorOrigenes.execute('call GetTopOrigen()')
    resOrigenes=cursorOrigenes.fetchall()
    contOrigen=[]
    for o in resOrigenes:
        contOrigen.append([o[0],o[1],o[2]])
    connection.close()
