from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Paciente, FichaM

# Create your views here.


def index(request):
    return HttpResponse("<h1>Hola Mundo!</h1>")


def info_paciente(request, rut):
    
    try:
        p = get_object_or_404(Paciente, rut_p=rut)
        m = "<h1>Nombre: " + p.nombres_p + "    Edad: " + \
            str(p.calcular_edad()) + "</h1><br>"
        fichas = p.ficham_set.all()   
 
        template = loader.get_template('info_paciente.html')
        context = {
            'p': p,
            'fichas': fichas
        }
    
    except Exception as e:
        p = "Error: No existe contenido"
        template = loader.get_template('info_paciente.html')
        context = {
            'p': p
        }    
        
    return HttpResponse(template.render(context, request))

def lista_pacientes(request):
    try:
        p = Paciente.objects.order_by('apellidos_p')
    #    template = loader.get_template('paciente.html')
     #   context = {
      #      'p' : p
       # }
    except Exception as e:
        p = "Hola"
    template = loader.get_template('paciente.html')
    context = {
        'p' : p
    }
    return HttpResponse(template.render(context, request))

def nuevo_paciente(request):
    template = loader.get_template('nuevoPaciente.html')
    context = {}
    return HttpResponse(template.render(context, request))

def crear_paciente(request):
    n = request.POST['nomb']
    a = request.POST['apellidos']
    r = request.POST['rut']
    if '.' in r or len(r) >10:
        mensaje = 'Error: el rut debe ir SIN PUNTOS y CON guion'
        return render(request, 'nuevoPaciente.html', {'msg':mensaje})
    
    f = request.POST['nacimiento']
   # f = f[6:]+'-'+f[:2]+'-'+f[3:5]
    s = request.POST['sexo']
    if s == 'masculino':
        s = 'M'
    elif s == 'femenino':
        s = 'F'
    e = request.POST['email']
    t = request.POST['fono']
    p = Paciente(
        nombres_p=n,
        apellidos_p=a,
        rut_p=r,
        sexo_p=s,
        telefono_p=t,
        fecha_nac_p=f,
        estado_p=1
    )
    try:
        pp = Paciente.objects.get(rut_p=r)
        mensaje = 'Error: el paciente ya se encuentra registrado'
        return render(request, 'nuevoPaciente.html', {'msg':mensaje})
    except:
        p.save()
        mensaje = 'Paciente creado con exito'
    return HttpResponseRedirect(reverse('lista'))

def nueva_ficha(request, rut):
    try:
        p = Paciente.objects.get(rut_p=rut)
    except:
        p = "Hola"
    template = loader.get_template('nueva_ficha.html')
    context = {
        'p' : p
    }
    return HttpResponse(template.render(context, request))

def crear_ficha(request, rut):
    p = get_object_or_404(Paciente, rut_p=rut)
    f = request.POST['fecha']
    a = f[:4]
    m = f[5:7]
    d = f[8:]
    diag = request.POST['diag']
    mot = request.POST['motivo']
    ficha = FichaM(dia_fhc_fm=d,mes_fch_fm=m,anio_fch_fm=a,paciente_fm=p,diagnostico_fm=diag,motivo_fm=mot)
    ficha.save()

    return HttpResponseRedirect(reverse('info_paciente',args=(p.rut_p,)))

def ficha(request, id, rut):
    f = get_object_or_404(FichaM, id=id)
    p = get_object_or_404(Paciente, rut_p=rut)
    template = loader.get_template('ficha.html')
    context = {
        'p': p,
        'ficha': f
    }
    
    return HttpResponse(template.render(context, request))