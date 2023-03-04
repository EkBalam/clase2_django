from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Pregunta


# Create your views here.
def index(request):
    # CONSULTAR LA BD ORM
    # SQL: Select * from pregunta order by desc fecha_pub limit 5
    ultimas_preguntas = Pregunta.objects.order_by('-fecha_pub')[:3]
    
    template = loader.get_template('polls/index.html')
    contexto = {
        'ultimas_preguntas':ultimas_preguntas
    }

    return HttpResponse(template.render(contexto, request))

def holamanuel(request):
    return HttpResponse("<h1> HOLA MANUEL </h1>")

def detalle(request, id_pregunta):
    return HttpResponse(f"Estas viendo la pregunta {id_pregunta}")

def resultados(request, id_pregunta):
    return HttpResponse(f'Estas viendo las respuestas de {id_pregunta}')

def votar(request, id_pregunta):
    return HttpResponse(f'Estas votando en {id_pregunta}')