from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

#from models import hotel,habitacion,reserva,servicio

# Create your views here.
def inicio(request):
    
    return render(request, "inicio.html")
    #return HttpResponse("VISTA DE INICIO")


def habitaciones(request):
    
    return HttpResponse("vista de habitaciones..")
