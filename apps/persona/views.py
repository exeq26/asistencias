from asistencias.apps.persona.models import Persona
from django.shortcuts import render

# Create your views here.

def listar_personas(request):
    personas = Persona.objects.all()
    return render(request, 'persona/lista_personas.html',{'personas':personas})

