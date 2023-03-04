from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Pregunta, Eleccion


# Create your views here.
def index(request):
    # CONSULTAR LA BD ORM
    # SQL: Select * from pregunta order by desc fecha_pub limit 5
    ultimas_preguntas = Pregunta.objects.order_by('-fecha_pub')[:10]
    
    template = loader.get_template('polls/index.html')
    contexto = {
        'ultimas_preguntas':ultimas_preguntas
    }

    return HttpResponse(template.render(contexto, request))

def holamanuel(request):
    return HttpResponse("<h1> HOLA MANUEL </h1>")

def detalle(request, id_pregunta):
    try:
        # Select * from pregunta where id = id_pregunta
        pregunta = Pregunta.objects.get(pk=id_pregunta)

        template = loader.get_template('polls/detalle.html')
        contexto = {
            'pregunta':pregunta
        }

        return HttpResponse(template.render(contexto, request))

    except Pregunta.DoesNotExist:
        raise Http404("La pregunta no existe")

def resultados(request, id_pregunta):
    pregunta = get_object_or_404(Pregunta, pk=id_pregunta)
    template = loader.get_template('polls/resultados.html')
    contexto = {
        'pregunta': pregunta
    }    
    return HttpResponse(template.render(contexto, request))

def votar(request, id_pregunta):
    pregunta = get_object_or_404(Pregunta, pk=id_pregunta)
    try:
        opcion_selccionada = Eleccion.objects.get(pk=request.POST["elegir"])
    except (KeyError, Eleccion.DoesNotExist):
        template_detalle = loader.get_template("polls/detalle.html")
        contexto = {
            'pregunta': pregunta,
            'mensaje_error': "La opción que elegiste no existe..."
        }
        return HttpResponse(template_detalle.render(contexto, request))
    else:
        opcion_selccionada.votos += 1
        opcion_selccionada.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:resultados', args=(pregunta.id, ) ))
# PARTE 4 https://docs.djangoproject.com/en/4.1/intro/tutorial04/