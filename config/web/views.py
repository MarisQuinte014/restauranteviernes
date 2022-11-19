from django.shortcuts import render
from web.formularios.formularioPlatos import FormularioRegistroPlatos
from web.formularios.formularioEmpleados import FormularioRegistroEmpleados
# Create your views here.

#CADA VISTA ES UNA FUNCION DE PY

def Home(request):
    return render(request,'index.html')

def Platos(request):

    #Cargar el formulario de registros de platos
    formulario = FormularioRegistroPlatos()

    #Creamos un diccionario para enviar datos hacia el template
    diccionarioEnvioDatos = {
        'formulario':formulario
    }

    #Recibiendo datos del formulario
    #PETICIÓN DE TIPO POST

    if request.method == 'POST':
        datosFormulario = FormularioRegistroPlatos(request.POST)
        if datosFormulario.is_valid():
            datosLimpios = datosFormulario.cleaned_data
            #ENVIANDO DATOS A MI BASE DE DATOS

    return render(request,'platos.html',diccionarioEnvioDatos)

def Empleados(request):

    formularioEmpleado = FormularioRegistroEmpleados()

    diccionarioEnvioDatosEmpleado = {
        'formularioEmpleado':formularioEmpleado
    }

    if request.method == 'POST':
        datosFormularioEmpleado = FormularioRegistroEmpleados(request.POST)
        if datosFormularioEmpleado.is_valid():
            datosLimpios = datosFormularioEmpleado.cleaned_data

    return render(request,'empleados.html',diccionarioEnvioDatosEmpleado)