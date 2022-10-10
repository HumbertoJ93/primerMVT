from re import template
from django.http import HttpResponse
import random 
from django.template import Template, Context, loader
from desafio.models import Persona
from datetime import date
from datetime import datetime




def primerview(request):
    
    return HttpResponse('Primer view')


def ver_personas(request):
    
    personas = Persona.objects.all()
    
    template = loader.get_template('ver_personas.html')
    template_renderizado = template.render({'personas': personas})
    
    return HttpResponse(template_renderizado)

def crear_persona(request):
    
    persona1 = Persona(nombre='Ana', apellido='Gonzalez', edad=random.randrange(1, 99), fecha_registro=datetime.now())
    persona2 = Persona(nombre='Humberto', apellido='Gonzalez', edad=random.randrange(1, 99), fecha_registro=datetime.now())
    persona3 = Persona(nombre='Yaine', apellido='Mavarez', edad=random.randrange(1, 99), fecha_registro=datetime.now())
    persona1.save()
    persona2.save()
    persona3.save()
    
    template = loader.get_template('crear_persona.html')
    template_renderizado = template.render({})
    
    return HttpResponse(template_renderizado)