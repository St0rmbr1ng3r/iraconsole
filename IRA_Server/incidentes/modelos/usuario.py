from django.db import models
from django.db import connection
from django.contrib.auth.hashers import make_password

#################################################
#   MODELO PARA USUARIO
#################################################

class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
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

    def eliminar_usuario(self,id_usuario):
        return 0

#################################################
#   MODELO PARA CREACION DE USUARIO
#################################################
class NuevoUsuario(models.Model):
    def guardar_usuario(self, formulario):

        passwd = formulario['password']
        is_superuser = formulario['is_superuser']
        username = formulario['username']
        first_name = formulario['first_name']
        last_name = formulario['last_name']
        email = formulario['email']
        is_active = formulario['is_active']

        print(formulario)

        if len(passwd) < 8:
            return 1            
        else:
            passwd = make_password(passwd)
            try:
                cursorCrearUsuario=connection.cursor()
                connection.commit()
                args = [passwd,is_superuser,username,first_name,last_name,email,is_active,]
                resCrearUsuario = cursorCrearUsuario.callproc('CrearUsuario', args)
                connection.close()
            except:
                return 1

        
        
