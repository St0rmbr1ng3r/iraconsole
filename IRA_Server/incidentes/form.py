from django import forms
from django.db import connection

class FormNuevoIncidente (forms.Form):

    BASICA=[('','--------'),(1,'NO'),(2,'SI')]

    ###############################
    # 1- CARGA MENU DE ORIGENES
    ###############################

    cursorOrigen=connection.cursor()
    cursorOrigen.execute('call GetOrigenes()')
    resOrigen=cursorOrigen.fetchall()
    opc_origenes=[('','--------')]
    for o in resOrigen:
        opc_origenes.append([o[0],o[1]])
    origen  = forms.ChoiceField(choices=opc_origenes,label='1- Orígen del Incidente')

    #########################################
    # 2- CARGA MENU TIPOSINCIDENTES
    #########################################

    cursorTipo=connection.cursor()
    cursorTipo.execute('call GetTiposIncidentes()')
    resTipos=cursorTipo.fetchall()
    opc_tipos=[('','--------')]
    for o in resTipos:
        opc_tipos.append([o[0],o[1]])
    tipoincidente  = forms.ChoiceField(choices=opc_tipos,label='2- Tipo de Incidente')

    #########################################
    # 3- DESCRIPCION DE EVENTOS
    #########################################

    descripcion = forms.CharField(max_length=200, widget=forms.Textarea,label='3- Descripción del Incidente')

    #########################################
    # 4- REGISTROS DE LA TABLA ETAPAS
    #########################################

    cursorEtapa=connection.cursor()
    cursorEtapa.execute('call GetEtapas()')
    resEtapas=cursorEtapa.fetchall()
    opc_etapas=[('','--------')]
    for o in resEtapas:
        opc_etapas.append([o[0],o[1]])
    etapa  = forms.ChoiceField(choices=opc_etapas,label='4- Etapa actual del Incidente')

    #########################################
    # 5- AFECTACION DE CLIENTES
    #########################################

    clientes = forms.ChoiceField(choices=BASICA,label='5- ¿Existe afectación de Cliente?')

    #########################################
    # 6- PROVEEDOR INVOLUCRADO
    #########################################

    proveedores = forms.ChoiceField(choices=BASICA,label='6- ¿Existen Proveedores Involucrados?')

    #########################################
    # 7- CARGA MENU ACTIVOS
    #########################################

    cursorActivo=connection.cursor()
    cursorActivo.execute('call GetActivos()')
    resActivos=cursorActivo.fetchall()
    opc_activos=[('','--------')]
    for o in resActivos:
        opc_activos.append([o[0],o[1]])
    activos  = forms.ChoiceField(choices=opc_activos,label='7- Activos Afectados')

    #########################################
    # 8- CARGA MENU AMBIENTES
    #########################################

    cursorAmbiente=connection.cursor()
    cursorAmbiente.execute('call GetAmbientes()')
    resAmbientes=cursorAmbiente.fetchall()
    opc_ambiente=[]
    for o in resAmbientes:
        opc_ambiente.append([o[0],o[1]])
    ambiente  = forms.MultipleChoiceField(choices=opc_ambiente,label='8- Ambientes Afectados',widget=forms.CheckboxSelectMultiple)


    #########################################
    # 9- CARGA MENU UBICACIONES
    #########################################

    cursorUbicacion=connection.cursor()
    cursorUbicacion.execute('call GetUbicaciones()')
    resUbicaciones=cursorUbicacion.fetchall()
    opc_ubicaciones=[]
    for o in resUbicaciones:
        opc_ubicaciones.append([o[0],o[1]])
    ubicacion  = forms.MultipleChoiceField(choices=opc_ubicaciones,label='9- Ubicaciones Afectadas',widget=forms.CheckboxSelectMultiple)

    #########################################
    # 10- CARGA MENU SERVICIOS
    #########################################

    cursorServicios=connection.cursor()
    cursorServicios.execute('call GetServicios()')
    resServicios=cursorServicios.fetchall()
    opc_servicios=[]
    for o in resServicios:
        opc_servicios.append([o[0],o[1]])
    servicio  = forms.MultipleChoiceField(choices=opc_servicios,label='10- Servicios Afectados',widget=forms.CheckboxSelectMultiple)

    #########################################
    # 11-  REGISTROS DE LA TABLA IMPACTOS
    #########################################

    cursorImpacto=connection.cursor()
    cursorImpacto.execute('call GetImpactos()')
    resImpactos=cursorImpacto.fetchall()
    opc_impactos=[('','--------')]
    for o in resImpactos:
        opc_impactos.append([o[0],o[1]])
    impacto  = forms.ChoiceField(choices=opc_impactos,label='11- Impacto del Incidente')

    #########################################
    # 12- REGISTROS DE LA TABLA URGENCIAS
    #########################################

    cursorUrgencia=connection.cursor()
    cursorUrgencia.execute('call GetUrgencias()')
    resUrgencias=cursorUrgencia.fetchall()
    opc_urgencias=[('','--------')]
    for o in resUrgencias:
        opc_urgencias.append([o[0],o[1]])
    activo  = forms.ChoiceField(choices=opc_urgencias,label='12- Urgencia del Incidente')
