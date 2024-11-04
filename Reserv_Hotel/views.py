from django.shortcuts import render
from datetime import datetime 
from django.http import HttpResponse, HttpResponseRedirect

from Reserv_Hotel.models import reserva
#from models import hotel,habitacion,reserva,servicio

# Create your views here.
def index(request):

    return render(request, "index.html")
    #return HttpResponse("VISTA DE INICIO")


def habitaciones(request):
    
    return HttpResponse("vista de habitaciones..")

def about(request):
    elements = range(1, 6)  # Genera una lista de números del 1 al 5
    return render(request, 'about.html', {'elements':elements})

def inicio(request):
    return render(request, "inicio.html")

def disponibles(request):
    #la intencion seria que muestre las habitaciones que esten disponibles, posiblemente ordenados por precio

    reserv = reserva.objects.all()
    print(reserv)

    return render(request, "disponibles.html", {'reserv': reserv})

#