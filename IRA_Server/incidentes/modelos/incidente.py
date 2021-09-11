from django.db import models
from django.forms import ModelForm
from django.db import connection

class Activos(models.Model):
    id_activo = models.IntegerField()
    desc_activo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'activos'


class Ambientes(models.Model):
    id_ambiente = models.IntegerField()
    desc_ambiente = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'ambientes'


class Comentarios(models.Model):
    id_comentario = models.IntegerField()
    id_inc = models.IntegerField()
    id_usuario = models.IntegerField()
    ts_comentario = models.DateTimeField()
    mensaje = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'comentarios'


class Criticidadesservicios(models.Model):
    id_criticidad_serv = models.IntegerField()
    desc_criticidad_serv = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'criticidadesservicios'


class Detallesambientes(models.Model):
    id_detalle_ambiente = models.IntegerField()
    id_inc = models.IntegerField()
    id_ambiente = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detallesambientes'


class Detallesservicios(models.Model):
    id_detalle_servicio = models.IntegerField()
    id_inc = models.IntegerField()
    id_servicio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detallesservicios'


class Detallesubicacion(models.Model):
    id_detalle_ubicacion = models.IntegerField()
    id_inc = models.IntegerField()
    id_ubicacion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detallesubicacion'


class Documentos(models.Model):
    id_documento = models.IntegerField()
    id_inc = models.IntegerField()
    titulo_doc = models.CharField(max_length=45)
    desc_documento = models.CharField(max_length=200)
    ruta_documento = models.CharField(max_length=100)
    ts_documento = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'documentos'


class Estados(models.Model):
    id_estado = models.IntegerField()
    desc_estado = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'estados'


class Etapas(models.Model):
    id_etapa = models.IntegerField()
    desc_etapa = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'etapas'


class Impactos(models.Model):
    id_impacto = models.IntegerField()
    desc_impacto = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'impactos'


class Incidentes(models.Model):

    id_inc = models.IntegerField()
    id_estado = models.IntegerField()
    id_etapa = models.IntegerField()
    id_tipo = models.IntegerField()
    id_origen = models.IntegerField()
    desc_inc = models.CharField(max_length=200)
    cli_afectados = models.IntegerField()
    prov_involucrado = models.IntegerField()
    act_afectados = models.IntegerField()
    id_impacto = models.IntegerField()
    id_urgencia = models.IntegerField()
    id_severidad = models.IntegerField()
    cont_comentarios = models.IntegerField()
    cont_documentos = models.IntegerField()
    ts_inc = models.DateTimeField()
    ts_cierre = models.DateTimeField(blank=True, null=True)
   
    class Meta:
        managed = False
        db_table = 'incidentes'


class Origenes(models.Model):
    id_origen = models.IntegerField()
    desc_origen = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'origenes'


class Servicios(models.Model):
    id_servicio = models.IntegerField()
    desc_servicio = models.CharField(max_length=45)
    id_criticidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'servicios'


class Severidades(models.Model):
    id_severidad = models.IntegerField()
    desc_severidad = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'severidades'


class Tiposincidentes(models.Model):
    id_tipo = models.IntegerField()
    desc_tipo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tiposincidentes'


class Ubicaciones(models.Model):
    id_ubicacion = models.IntegerField()
    desc_ubicacion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'ubicaciones'


class Urgencias(models.Model):
    id_urgencia = models.IntegerField()
    desc_urgencia = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'urgencias'

class Multicheck(models.Model):
    ambiente = models.CharField(max_length=45)
    ubicacion = models.CharField(max_length=45)
    servicio = models.CharField(max_length=45)

class IncidentesActivos(models.Model):
    cursorIncActivos=connection.cursor()
    cursorIncActivos.execute('call GetIncidentesActivosListado()')
    resIncActivos=cursorIncActivos.fetchall()
    connection.close()

#################################################
#   NUEVO MODELO PARA GUARDAR INCIDENTES
#################################################


class NuevoIncidente(models.Model):

    def guardar_incidente(self, formulario):

        id_etapa = formulario['id_etapa']
        id_tipo = formulario['id_tipo']
        id_origen = formulario['id_origen']
        desc_inc = formulario['desc_inc']
        cli_afectados = formulario['cli_afectados']
        prov_involucrado = formulario['prov_involucrado']
        act_afectados = formulario['act_afectados']
        id_impacto = formulario['id_impacto']
        id_urgencia = formulario['id_urgencia']
        id_severidad = formulario['id_severidad']
        args=[id_etapa, id_tipo, id_origen, desc_inc, cli_afectados, prov_involucrado,	act_afectados,	id_impacto,	id_urgencia, id_severidad,]

        cursorGuardarIncidente=connection.cursor()
        resGuardarIncidente = cursorGuardarIncidente.callproc('GuardarNuevoIncidente', args)

        cursorUltimoIncidente=connection.cursor()
        cursorUltimoIncidente.execute('call GetOrigenes()')
        res = cursorUltimoIncidente.fetchall()
        nuevo_id = res[0]
        connection.close()
        print(nuevo_id)