from django.shortcuts import render
from datetime import datetime 
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from Reserv_Hotel.formularios import formulario_reserva


from Reserv_Hotel.models import reserva, hotel
#from models import hotel,habitacion,reserva,servicio

# Create your views here.
def inicio(request):
    reserv = reserva.objects.filter(reservado = False)
    print(reserv)
    return render(request, "inicio.html", {'reserv': reserv})
    #return HttpResponse("VISTA DE INICIO")


def habitaciones(request):
    
    return HttpResponse("vista de habitaciones..")

def Hoteles(request):
    elements = hotel.objects.all()

    print(elements)
    return render(request, 'Hotel.html', {'elements':elements})

def inicio1(request):
    return render(request, "inicio1.html")

def disponibles(request):

    #la intencion seria que muestre las habitaciones que esten disponibles, posiblemente ordenados por precio

    reserv = reserva.objects.all()
    print(reserv)

    return render(request,"reservados.html",  {'reserv': reserv})


def form_reserva(request):

    if request.method == "POST":
        formulario = formulario_reserva(request.POST)
        
        print("formulario: ")
        print(formulario)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            print(f"Datos: {datos}")
            nuevo = reserva(**datos)
            nuevo.save()
            return render(request, "inicio.html")

    formulario = formulario_reserva()
    return render(request,"formreserva.html", {"reserv": formulario})



