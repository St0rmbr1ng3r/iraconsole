from django.db import models

"""
##################
#MODELO DE ACTIVO
##################
class activo(models.Model):
    id_activo=models.IntegerField()
    desc_activo=models.CharField(max_length=45)
    class Meta:
        db_table:"activos"

#####################
#MODELO DE AMBIENTE
#####################
class ambiente(models.Model):
    id_ambiente=models.IntegerField()
    desc_ambiente=models.CharField(max_length=45)
    class Meta:
        db_table:"ambientes"

#####################
#MODELO DE COMENTARIO
#####################
class comentario(models.Model):
    id_comentario=models.IntegerField()
    id_inc=models.IntegerField()
    id_usuario=models.IntegerField()
    ts_comentario=models.DateField()
    mensaje=models.CharField(max_length=200)
    class Meta:
        db_table:"comentarios"

#####################################
#MODELO DE CRITICIDAD DE SERVICIO
#####################################
class criticidadservicio(models.Model):
    id_criticidad_servicio=models.IntegerField()
    desc_critividad_servicio=models.CharField(max_length=45)
    class Meta:
        db_table:"criticidadesservicios"

###########################
#MODELO DE DOCUMENTO
###########################
class documento(models.Model):
    id_documento=models.IntegerField()
    id_inc=models.IntegerField()
    titulo_docu=models.CharField(max_length=45)
    desc_origen=models.CharField(max_length=200)
    ruta_documento=models.CharField(max_length=100)
    ts_documento=models.DateField()
    class Meta:
        db_table:"documentos"

######################
#MODELO DE ESTADO
######################
class estado(models.Model):
    id_estado=models.IntegerField()
    desc_estado=models.CharField(max_length=45)
    class Meta:
        db_table:"estados"

#####################
#MODELO DE ETAPAS
#####################
class etapa(models.Model):
    id_etapa=models.IntegerField()
    desc_oetapa=models.CharField(max_length=45)
    class Meta:
        db_table:"etapas"

#####################
#MODELO DE IMPACTO
#####################
class impacto(models.Model):
    id_impacto=models.IntegerField()
    desc_impacto=models.CharField(max_length=45)
    class Meta:
        db_table:"impactos"

######################
#MODELO DE ORIGEN
######################
class origen(models.Model):
    id_origen=models.IntegerField()
    desc_origen=models.CharField(max_length=45)
    class Meta:
        db_table:"origenes"

######################
#MODELO DE SERVICIO
######################
class servicio(models.Model):
    id_servicio=models.IntegerField()
    desc_servicio=models.CharField(max_length=45)
    id_criticidad=models.IntegerField()
    class Meta:
        db_table:"servicios"

######################
#MODELO DE SEVERIDAD
######################
class severidad(models.Model):
    id_severidad=models.IntegerField()
    desc_severidad=models.CharField(max_length=45)
    class Meta:
        db_table:"severidades"

################################
#MODELO DE TIPO DE INCIDENTE
################################
class tipoincidente(models.Model):
    id_tipo=models.IntegerField()
    desc_tipo=models.CharField(max_length=45) 
    class Meta:
        db_table:"tiposincidentes"

################################
#MODELO DE UBICACIÓN
################################
class ubicacion(models.Model):
    id_ubicacion=models.IntegerField()
    desc_ubicacion=models.CharField(max_length=45)
    class Meta:
        db_table:"ubicaciones"

################################
#MODELO DE URGENCIA
################################
class urgencia(models.Model):
    id_urgencia=models.IntegerField()
    desc_urgencia=models.CharField(max_length=45)
    class Meta:
        db_table:"urgencias"

################################
#MODELO DE INCIDENTE
################################

"""


class Activos(models.Model):
    id_activo = models.AutoField(primary_key=True)
    desc_activo = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'activos'


class Ambientes(models.Model):
    id_ambiente = models.AutoField(primary_key=True)
    desc_ambiente = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'ambientes'



class Comentarios(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    id_inc = models.ForeignKey('Incidentes', models.DO_NOTHING, db_column='id_inc')
    id_usuario = models.IntegerField()
    ts_comentario = models.DateTimeField()
    mensaje = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'comentarios'


class Criticidadesservicios(models.Model):
    id_criticidad_serv = models.AutoField(primary_key=True)
    desc_criticidad_serv = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'criticidadesservicios'


class Detallesambientes(models.Model):
    id_detalle_ambiente = models.AutoField(primary_key=True)
    id_inc = models.ForeignKey('Incidentes', models.DO_NOTHING, db_column='id_inc')
    id_ambiente = models.ForeignKey(Ambientes, models.DO_NOTHING, db_column='id_ambiente')

    class Meta:
        managed = True
        db_table = 'detallesambientes'


class Detallesservicios(models.Model):
    id_detalle_servicio = models.AutoField(primary_key=True)
    id_inc = models.ForeignKey('Incidentes', models.DO_NOTHING, db_column='id_inc')
    id_servicio = models.ForeignKey('Servicios', models.DO_NOTHING, db_column='id_servicio')

    class Meta:
        managed = True
        db_table = 'detallesservicios'


class Detallesubicacion(models.Model):
    id_detalle_ubicacion = models.AutoField(primary_key=True)
    id_inc = models.ForeignKey('Incidentes', models.DO_NOTHING, db_column='id_inc')
    id_ubicacion = models.ForeignKey('Ubicaciones', models.DO_NOTHING, db_column='id_ubicacion')

    class Meta:
        managed = True
        db_table = 'detallesubicacion'


class Documentos(models.Model):
    id_documento = models.AutoField(primary_key=True)
    id_inc = models.ForeignKey('Incidentes', models.DO_NOTHING, db_column='id_inc')
    titulo_doc = models.CharField(max_length=45)
    desc_documento = models.CharField(max_length=200)
    ruta_documento = models.CharField(max_length=100)
    ts_documento = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'documentos'
        unique_together = (('id_documento', 'id_inc'),)


class Estados(models.Model):
    id_estado = models.AutoField(primary_key=True)
    desc_estado = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'estados'


class Etapas(models.Model):
    id_etapa = models.AutoField(primary_key=True)
    desc_etapa = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'etapas'


class Impactos(models.Model):
    id_impacto = models.AutoField(primary_key=True)
    desc_impacto = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'impactos'


class Incidentes(models.Model):
    id_inc = models.AutoField(primary_key=True)
    id_estado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='id_estado')
    id_etapa = models.ForeignKey(Etapas, models.DO_NOTHING, db_column='id_etapa')
    id_tipo = models.ForeignKey('Tiposincidentes', models.DO_NOTHING, db_column='id_tipo')
    id_origen = models.ForeignKey('Origenes', models.DO_NOTHING, db_column='id_origen')
    desc_inc = models.CharField(max_length=200)
    cli_afectados = models.IntegerField()
    prov_involucrado = models.IntegerField()
    act_afectados = models.IntegerField()
    id_impacto = models.ForeignKey(Impactos, models.DO_NOTHING, db_column='id_impacto')
    id_urgencia = models.ForeignKey('Urgencias', models.DO_NOTHING, db_column='id_urgencia')
    id_severidad = models.ForeignKey('Severidades', models.DO_NOTHING, db_column='id_severidad')
    cont_comentarios = models.IntegerField()
    cont_documentos = models.IntegerField()
    ts_inc = models.DateTimeField()
    ts_cierre = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'incidentes'





class Origenes(models.Model):
    id_origen = models.AutoField(primary_key=True)
    desc_origen = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'origenes'


class Servicios(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    desc_servicio = models.CharField(max_length=45)
    id_criticidad = models.ForeignKey(Criticidadesservicios, models.DO_NOTHING, db_column='id_criticidad')

    class Meta:
        managed = True
        db_table = 'servicios'


class Severidades(models.Model):
    id_severidad = models.AutoField(primary_key=True)
    desc_severidad = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'severidades'


class Tiposincidentes(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    desc_tipo = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'tiposincidentes'


class Ubicaciones(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    desc_ubicacion = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'ubicaciones'


class Urgencias(models.Model):
    id_urgencia = models.AutoField(primary_key=True)
    desc_urgencia = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'urgencias'
