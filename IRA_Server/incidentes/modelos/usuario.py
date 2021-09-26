from django.db import models
from django.db import connection

#################################################
#   MODELO PARA TABLA DE INCIDENTES ACTIVOS
#################################################

class Usuario(models.Model):

    def listar_usuarios_activos():
        cursorUsuariosActivos=connection.cursor()
        cursorUsuariosActivos.execute('call GetUsuariosActivos()')
        resUsuariosActivos=cursorUsuariosActivos.fetchall()
        connection.close()
        return resUsuariosActivos

    