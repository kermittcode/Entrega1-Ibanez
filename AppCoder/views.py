from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso, Profesor, Estudiante, Entregable
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario

# Create your views here.



def inicio(request):

    return render(request, 'AppCoder/inicio.html')

def curso(request):
    
    curso = Curso(nombre= 'Desarrollo web', generacion = '40150')
    
    curso.save()

    texto = f'---> Curso: {curso.nombre}, Generacion: {curso.generacion}'

    return render(request, 'AppCoder/cursos.html')

def profesores(request):

    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):

    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):

    return render(request, 'AppCoder/entregables.html')

def curso_formulario(request):
    
    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST)

        print(miFormulario)           

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            curso = Curso (nombre=informacion['curso'], generacion=informacion['generacion'])

            curso.save()

            return render(request, 'AppCoder/inicio.html')

    else:

        miFormulario= CursoFormulario()

    return render(request, 'AppCoder/curso_formulario.html', {'miFormulario':miFormulario})

def profesor_formulario(request):

    if request.method == 'POST':

        miFormulario2 = ProfesorFormulario(request.POST)

        print(miFormulario2)

        if miFormulario2.is_valid:

            informacion = miFormulario2.cleaned_data

            profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])
            
            profesor.save()

            return render(request, 'AppCoder/inicio.html')   

    else:

        miFormulario2= ProfesorFormulario()

    return render(request, 'AppCoder/profesor_formulario.html', {'miFormulario':miFormulario2})

def busqueda_generacion(request):

    return render(request, 'AppCoder/busqueda_generacion.html')

def buscar(request):

    if request.GET["generacion"]:

        generacion = request.GET["generacion"]
        cursos = Curso.objects.filter(generacion__icontains=generacion)

        return render(request, "AppCoder/resultados_busqueda.html", {"cursos":cursos, "generacion":generacion})
   
    else:
        
        respuesta = 'No enviaste datos'

    return HttpResponse(respuesta)


def estudiante_formulario(request):

    if request.method == 'POST':

        miFormulario3 = EstudianteFormulario(request.POST)

        print(miFormulario3)

        if miFormulario3.is_valid:

            informacion = miFormulario3.cleaned_data

            estudiante = Estudiante (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            
            estudiante.save()

            return render(request, 'AppCoder/inicio.html')   

    else:

        miFormulario3= EstudianteFormulario()

    return render(request, 'AppCoder/estudiante_formulario.html', {'miFormulario':miFormulario3})