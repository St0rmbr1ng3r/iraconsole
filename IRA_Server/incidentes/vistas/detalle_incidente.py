from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ..modelos.incidente import Incidentes
from ..modelos.formularios import FormularioDetalleIncidente,FormularioModificarIncidente
from django.contrib import messages


@login_required(login_url='login')
def cargar_incidente(request):
    if request.method == 'GET':
        id_inc=request.GET.get('id_inc', '0')

        i = Incidentes()
        detalle = i.cargar_detalle_incidente(id_inc)
        if detalle == 1:
            messages.error(request, "Incidente Invalido")
            return redirect('activos')
        
        print(detalle)
        
        formulario = FormularioDetalleIncidente(initial={
            'id_inc' : int(detalle[0][0]), 
            'id_estado' : int(detalle[0][1]), 
            'id_etapa' : int(detalle[0][2]), 
            'id_tipo' :int(detalle[0][3]), 
            'id_origen' : int(detalle[0][4]), 
            'desc_inc' : detalle[0][5], 
            'cli_afectados' : int(detalle[0][6]), 
            'prov_involucrado' : int(detalle[0][7]), 
            'act_afectados' : int(detalle[0][8]), 
            'id_impacto' :int(detalle[0][9]), 
            'id_urgencia' : int(detalle[0][10]), 
            'id_severidad' : int(detalle[0][11]), 
            'cont_comentarios' : int(detalle[0][12]), 
            'cont_documentos' : int(detalle[0][13]), 
            'ts_inc' : detalle[0][14],
            'ts_cierre' : detalle[0][15],
            'ambiente' : detalle[0][16]
            
        })
        contexto = {'formulario':formulario}
        return render(request, "detalle_incidente.html", contexto)


@login_required(login_url='login')
def no_encontrado(request):
    return render(request, "sinresultado.html")
