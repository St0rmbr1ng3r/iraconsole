from django.db import models
from django.db import connection
from django.forms import widgets
from django.forms.widgets import Widget
from django import forms

#################################################
#   MODELO PARA USUARIO
#################################################

class Usuario(models.Model):
    id = models.IntegerField()
    password = models.CharField()
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

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

    def guardar_usuario(self):
        print ("formulario de usuario es valido")
