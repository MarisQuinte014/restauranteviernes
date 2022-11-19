from django.shortcuts import render
from web.formularios.formularioPlatos import FormularioRegistroPlatos
from web.formularios.formularioEmpleados import FormularioRegistroEmpleados
from web.models import Platos, Empleados
# Create your views here.

#CADA VISTA ES UNA FUNCION DE PY

def Home(request):
    return render(request,'index.html')

def PlatosVista(request):

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
            platoNuevo = Platos(
                nombre = datosLimpios["nombrePlato"],
                descripcion = datosLimpios["descripcionPlato"],
                imagen = datosLimpios["fotoPlato"],
                precio = datosLimpios["precioPlato"],
                tipo = datosLimpios["tipoPlato"]
            )
            platoNuevo.save()

    return render(request,'platos.html',diccionarioEnvioDatos)

def EmpleadosVista(request):

    formularioEmpleado = FormularioRegistroEmpleados()

    diccionarioEnvioDatosEmpleado = {
        'formularioEmpleado':formularioEmpleado
    }

    if request.method == 'POST':
        datosFormularioEmpleado = FormularioRegistroEmpleados(request.POST)
        if datosFormularioEmpleado.is_valid():
            datosLimpiosEmpleado = datosFormularioEmpleado.cleaned_data
            empleadoNuevo = Empleados(
                nombre = datosLimpiosEmpleado["nombre"],
                apellido = datosLimpiosEmpleado["apellido"],
                cargo = datosLimpiosEmpleado["cargo"],
                direccion = datosLimpiosEmpleado["direccion"],
                telefono = datosLimpiosEmpleado["telefono"],
            )
            empleadoNuevo.save()

    return render(request,'empleados.html',diccionarioEnvioDatosEmpleado)