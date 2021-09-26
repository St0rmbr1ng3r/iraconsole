from django.db import models
from django.db import connection

#################################################
#   MODELO PARA TABLA DE INCIDENTES ACTIVOS
#################################################

class Usuario(models.Model):

    def listar_usuarios_activos(self):
        cursorUsuariosActivos=connection.cursor()
        cursorUsuariosActivos.execute('call GetUsuariosActivos()')
        resUsuariosActivos=cursorUsuariosActivos.fetchall()
        connection.close()
        return resUsuariosActivos

    def cargar_detalle_usuario(self,id_usuario):
        try:
            cursorDetalleUsuario = connection.cursor()
            args = [int(id_usuario)]
            cursorDetalleUsuario.callproc('GetDetalleUsuario',args)
            result=cursorDetalleUsuario.fetchall()
            if result:
                return result
            else:
                return 1
        except:
            print("Error al traer detalle de Usuario")
            return 1