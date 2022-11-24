from django.shortcuts import render
from AppFamily.models import Familia
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def familia(request):
    padre = Familia(nombre="Pedro",edad=67,nacimiento="1965-3-19") 
    madre = Familia(nombre="Rosa",edad=60,nacimiento="1962-3-6") 
    hermano = Familia(nombre="Ignacio",edad=23,nacimiento="1999-4-12") 
    padre.save()
    madre.save()
    hermano.save()

    dic = { "nombrePadre": padre.nombre,
        "edadPadre": padre.edad,
        "nacimientoPadre": padre.nacimiento,
        "nombreMadre": madre.nombre,
        "edadMadre": madre.edad,
        "nacimientoMadre": madre.nacimiento,
        "nombreHermano": hermano.nombre,
        "edadHermano": hermano.edad,
        "nacimientoHermano": hermano.nacimiento }
       #Diccionario del cual se van a sacar los datos para el HTML (Voy a usar la clave siempre)
    
    plantilla = loader.get_template("template1.html") #Llamo al template 

    doc = plantilla.render(dic)
    return HttpResponse(doc)