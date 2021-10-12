from django.forms import ModelForm
from .incidente import Incidentes
from .incidente import Multicheck
from .usuario import Usuario
from django.db import connection
from django import forms

class FormularioIncidente(ModelForm):
    class Meta:
        model = Incidentes
        fields =  ['id_etapa','id_tipo','id_origen','desc_inc','cli_afectados','prov_involucrado','act_afectados','id_impacto',
        'id_urgencia','id_severidad'] 
        #fields = '__all__' PARA UTILIZAR TODOS LOS CAMPOS

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
    id_origen  = forms.ChoiceField(choices=opc_origenes,label='1- Orígen del Incidente')
    connection.close()

    #########################################
    # 2- CARGA MENU TIPOS DE INCIDENTE
    #########################################

    cursorTipo=connection.cursor()
    cursorTipo.execute('call GetTiposIncidentes()')
    resTipos=cursorTipo.fetchall()
    opc_tipos=[('','--------')]
    for o in resTipos:
        opc_tipos.append([o[0],o[1]])
    id_tipo  = forms.ChoiceField(choices=opc_tipos,label='2- Tipo de Incidente')
    connection.close()

    #########################################
    # 3- CUADRO DESCRIPCIÓN INCIDENTE
    #########################################

    desc_inc = forms.CharField(max_length=200, widget=forms.Textarea,label='3- Descripción del Incidente')

    #########################################
    # 4- CARGA MENU ETAPAS
    #########################################

    cursorEtapa=connection.cursor()
    cursorEtapa.execute('call GetEtapas()')
    resEtapas=cursorEtapa.fetchall()
    opc_etapas=[('','--------')]
    for o in resEtapas:
        opc_etapas.append([o[0],o[1]])
    id_etapa  = forms.ChoiceField(choices=opc_etapas,label='4- Etapa actual del Incidente')
    connection.close()

    #########################################
    # 5- CARGA MENU AFECTACION DE CLIENTES
    #########################################

    cli_afectados = forms.ChoiceField(choices=BASICA,label='5- ¿Existe afectación de Cliente?')

    #########################################
    # 6- CARGA MENU PROVEEDOR INVOLUCRADO
    #########################################

    prov_involucrado = forms.ChoiceField(choices=BASICA,label='6- ¿Existen Proveedores Involucrados?')

    #########################################
    # 7- CARGA MENU ACTIVOS
    #########################################

    cursorActivo=connection.cursor()
    cursorActivo.execute('call GetActivos()')
    resActivos=cursorActivo.fetchall()
    opc_activos=[('','--------')]
    for o in resActivos:
        opc_activos.append([o[0],o[1]])
    act_afectados  = forms.ChoiceField(choices=opc_activos,label='7- Activos Afectados')
    connection.close()

    #########################################
    # 11-  CARGA MENU IMPACTOS
    #########################################

    cursorImpacto=connection.cursor()
    cursorImpacto.execute('call GetImpactos()')
    resImpactos=cursorImpacto.fetchall()
    opc_impactos=[('','--------')]
    for o in resImpactos:
        opc_impactos.append([o[0],o[1]])
    id_impacto  = forms.ChoiceField(choices=opc_impactos,label='11- Impacto del Incidente')
    connection.close()

    #########################################
    # 12- CARGA MENU URGENCIAS
    #########################################

    cursorUrgencia=connection.cursor()
    cursorUrgencia.execute('call GetUrgencias()')
    resUrgencias=cursorUrgencia.fetchall()
    opc_urgencias=[('','--------')]
    for o in resUrgencias:
        opc_urgencias.append([o[0],o[1]])
    id_urgencia  = forms.ChoiceField(choices=opc_urgencias,label='12- Urgencia del Incidente')
    connection.close()

    #########################################
    # 13- CARGA MENU SEVERIDADES
    #########################################

    cursorSeveridades=connection.cursor()
    cursorSeveridades.execute('call GetSeveridades()')
    resSeveridadess=cursorSeveridades.fetchall()
    opc_severidades=[('','--------')]
    for o in resSeveridadess:
        opc_severidades.append([o[0],o[1]])
    id_severidad  = forms.ChoiceField(choices=opc_severidades,label='12- Severidad del Incidente')
    connection.close()

class FormularioMulti(ModelForm):
    class Meta:
        model = Multicheck
        fields =  ['ambiente','ubicacion','servicio'] 
        #fields = '__all__' PARA UTILIZAR TODOS LOS CAMPOS

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
    connection.close()

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
    connection.close()

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
    connection.close()

   

class FormularioUsuario(ModelForm):
    class Meta:
        model = Usuario
        fields =  ['password','is_superuser','username','first_name','last_name','is_active','email'] 

    BASICA=[('','--------'),(0,'NO'),(1,'SI')]

    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(max_length=150, widget=forms.TextInput)
    first_name = forms.CharField(max_length=150, widget=forms.TextInput)
    last_name = forms.CharField(max_length=150, widget=forms.TextInput)
    email = forms.EmailField(max_length=254, widget=forms.EmailInput)

    #SELECCION PARA DEJAR USUARIO ACTIVO EN EL SISTEMA
    is_active = forms.ChoiceField(choices=BASICA,label='Habilitar Usuario?')

    #SELECCION PARA DEJAR USUARIO COMO ADMINISTRADOR
    is_superuser = forms.ChoiceField(choices=BASICA,label='Usuario Administrador?')

