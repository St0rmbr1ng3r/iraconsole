from django.db import models
from django.db import connection


class Comentarios(models.Model):
    id_comentario = models.IntegerField()
    id_inc = models.IntegerField()
    id_usuario = models.IntegerField()
    ts_comentario = models.DateTimeField()
    mensaje = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'comentarios'


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

class Incidentes(models.Model):

    id_inc = models.IntegerField(primary_key=True)
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
    ts_cierre = models.DateTimeField()

    def cargar_detalle_incidente(self,id_inc):
        try:
            cursorDetalleIncidente = connection.cursor()
            args = [int(id_inc),]
            cursorDetalleIncidente.callproc('GetDetalleIncidente',args)
            result=cursorDetalleIncidente.fetchall()
            connection.close()
            if result:
                return result
            else:
                return 1
        except:
            print("Error al traer detalle de Incidente")
            return 1

    def cargar_detalle_ambiente(self,id_inc):
        try:
            cursorDetalleAmbiente = connection.cursor()
            args = [int(id_inc),]
            cursorDetalleAmbiente.callproc('GetDetalleAmbiente',args)
            result=cursorDetalleAmbiente.fetchall()
            connection.close()
            if result:
                return result
            else:
                return 1
        except:
            print("Error al traer detalle del Ambiente")
            return 1


class Multicheck(models.Model):
    ambiente = models.CharField(max_length=45)
    ubicacion = models.CharField(max_length=45)
    servicio = models.CharField(max_length=45)

#################################################
#   MODELO PARA TABLA DE INCIDENTES ACTIVOS
#################################################

class IncidentesActivos(models.Model):
    def listar_incidentes_activos(self):
        cursorIncActivos=connection.cursor()
        cursorIncActivos.execute('call GetIncidentesActivosListado()')
        resIncActivos=cursorIncActivos.fetchall()
        connection.close()
        return resIncActivos


#################################################
#   MODELO PARA GUARDAR INCIDENTES
#################################################

class NuevoIncidente(models.Model):

    def guardar_detalle_ambiente(self, ambiente, nuevo_id):      
        try:
            cursorDetalleAmbiente = connection.cursor()
            connection.commit()
            for a in ambiente:
                args = [nuevo_id,a,]
                resDetalleAmbiente = cursorDetalleAmbiente.callproc('GuardarDetalleAmbiente', args)
            connection.close()
            return 0
        except:
            print("Error al guardar detalles de ambientes")
            return 1
 
    def guardar_detalle_ubicacion(self, ubicacion, nuevo_id):          
        try:
            cursorDetalleUbicacion = connection.cursor()
            connection.commit()
            for u in ubicacion: #ITERO POR CADA UBICACION AGREGADA
                args = [nuevo_id,u,]
                resDetalleUbicacion = cursorDetalleUbicacion.callproc('GuardarDetalleUbicacion', args)
            connection.close()
            return 0
        except:
            print("Error al guardar detalles de ubicaciones")
            return 1

    def guardar_detalle_servicio(self, servicio, nuevo_id):          
        try:
            cursorDetalleServicio = connection.cursor()
            connection.commit()
            for s in servicio:
                args = [nuevo_id,s,]
                resDetalleServicio = cursorDetalleServicio.callproc('GuardarDetalleServicio', args)
            connection.close()
            return 0
        except:
            print("Error al guardar detalles de servicios")
            return 1

    def guardar_incidente(self, formulario, formulariomulti):

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

        nuevo_id = 0

        ambiente = formulariomulti['ambiente']
        ubicacion = formulariomulti['ubicacion']
        servicio = formulariomulti['servicio']
        
        #SE COMIENZA GUARDANDO LA PARTE CENTRAL DEL INCIDENTE Y LUEGO LOS DETALLES
        try:
            cursorGuardarIncidente=connection.cursor()
            connection.commit()
            args = [id_etapa, id_tipo, id_origen, desc_inc, cli_afectados, prov_involucrado,	act_afectados,	id_impacto,	id_urgencia, id_severidad,]
            resGuardarIncidente = cursorGuardarIncidente.callproc('GuardarNuevoIncidente', args)
            connection.close()
        except:
            return 1
        else:
            try:
                #OBTENGO EL ID DEL NUEVO INCIDENTE
                cursorUltimoIncidente=connection.cursor()
                cursorUltimoIncidente.execute('call GetUltimoIncidente()')
                res = cursorUltimoIncidente.fetchall()
                nuevo_id = res[0][0] 
                connection.close()
            except:
                return 1
            else:
                #GUARDADO DE LOS DETALLES DE AMBIENTES; UBICACION Y SERVICIOS
                if self.guardar_detalle_ambiente(ambiente, nuevo_id) == 0:
                    if self.guardar_detalle_ubicacion(ubicacion, nuevo_id) == 0:
                        if self.guardar_detalle_servicio(servicio, nuevo_id) == 0:
                            print("Detalles guardados correctamente")
                            return 0
                        else:
                            print("Fallo el detalle del servicio")
                            return 1
                    else:
                        print("Fallo el detalle de la ubicacion")
                        return 1
                else:
                    print("Fallo el detalle del ambiente")
                    return 1
                

#################################################
#   MODELO PARA DETALLE DE UN INCIDENTE
#################################################

class DetalleIncidente(models.Model):
    def buscar_incidente(self, id_inc):      
        try:
            cursorDetalleIncidente = connection.cursor()
            args = [int(id_inc)]
            cursorDetalleIncidente.callproc('GetDetalleIncidente',args)
            result=cursorDetalleIncidente.fetchall()
            if result:
                return result
            else:
                return 1
        except:
            print("Error al traer detalle de incidente")
            return 1

    def buscar_detalle_incidente(self, id_inc):
        detallesMultiples = []
        print("PRIMERA: ",detallesMultiples)
        print("ID INCIDENTE: ", id_inc)
        try:
            cursorDetalleAmbienteInc = connection.cursor()
            args = [int(id_inc)]
            cursorDetalleAmbienteInc.callproc('GetDetalleAmbiente',args)
            resultado=cursorDetalleAmbienteInc.fetchall()
            detallesMultiples.append(resultado)
            print("PRIMER ELEMENTO ", detallesMultiples)
            try:
                cursorDetalleUbicacionInc = connection.cursor()
                args = [int(id_inc)]
                cursorDetalleUbicacionInc.callproc('GetDetalleUbicacion',args)
                resultado=cursorDetalleUbicacionInc.fetchall()
                detallesMultiples.append(resultado)
                print("SEGUNDO ELEMENTO ", detallesMultiples)
                try:
                    cursorDetalleServicioInc = connection.cursor()
                    args = [int(id_inc)]
                    cursorDetalleServicioInc.callproc('GetDetalleServicio',args)
                    resultado=cursorDetalleServicioInc.fetchall()
                    detallesMultiples.append(resultado)
                    print("TERCER ELEMENTO ", detallesMultiples)
                    return detallesMultiples
                except:
                    print("FALLO SERVICIOS")
                    return 1
            except:
                print("FALLO UBICACION")
                return 1
        except:
            print("FALLO AMBIENTE")

            return 1