from django.shortcuts import render, redirect, get_object_or_404 #404 busca un elemento
from django.contrib.auth.models import User # importamos el modelo user para usarlo en el login

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login
from .formularios import formulario_reserva, formulario_hotel, form_habitacion, customusercreateform

from django.contrib.auth.decorators import login_required
from .models import reserva, hoteles, habitacion
#from models import hotel,habitacion,reserva,servicio

# Create your views here.
def inicio(request):
    reserv = reserva.objects.filter(reservado = False)
    print(reserv)
    return render(request, "inicio.html", {'reserv': reserv})
    #return HttpResponse("VISTA DE INICIO")


def habitaciones(request):# muestra habitaciones disponibles

    elementos = habitacion.objects.filter(ocupado=True)
    print(elementos)
    return render(request, "inicio.html",{'element': elementos})


def Hoteles(request):
    elements = hoteles.objects.all()
    print(elements)
    return render(request, 'Hotel.html', {'elements':elements})

def soporte(request):
    return render(request,"Soporte.html")

@login_required
def reservadoss(request):

    #la intencion seria que muestre las habitaciones que esten disponibles, posiblemente ordenados por precio
    #aqui se listaran todas las reservas que halla hecho el usuario comparando su id o su dni

    reserv = reserva.objects.all()
    

    return render(request,"reservados.html",  {'reserv': reserv})

@login_required
def form_reserva(request):

    if request.method == "POST":
        formulario = formulario_reserva(request.POST)
        
        print("el usuario que ingreso es: ")
        print()
        
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            print(f"Datos: {datos}")
            nuevo = reserva(**datos)
            nuevo.save()
            return render(request, "inicio.html")

    formulario = formulario_reserva()
    return render(request,"formreserva.html", {"reserv": formulario})


def form_hotel(request):
    
    if request.method == "POST":
        formulario = formulario_hotel(request.POST, request.FILES)
        print("formulario: ")
        if formulario.is_valid():
            datos = formulario.cleaned_data
            print(f"Datos: {datos}")
            nuevo = hoteles(**datos)
            nuevo.save()
            return render(request, "inicio.html")

    formulario = formulario_hotel()
    return render(request,"formhotel.html", {"nuevo_h": formulario})

def information(request):
    return render(request, "informacion.html")


def nueva_habit(request):

    if request.method == "POST":
        formulario = form_habitacion(request.POST)
        if formulario.is_valid():
            datos=formulario.cleaned_data
            nuevo = habitacion(**datos)
            nuevo.save()
            return render(request, "inicio.html")
    formulario = form_habitacion()
    return render(request, "nueva_habitacion.html", {"nuevo_ha":formulario})

def registro(request):
    data = {
        "form": customusercreateform()
    }
    if request.method == "POST":
        formulario = customusercreateform(data =request.POST)
        if formulario.is_valid():
            formulario.save()
            #autentica el usuario
            print("se registro correctamente")
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            #dirigir al inicio
            return redirect(to="inicio")
        data["form"] = formulario

    return render(request, "registration/registro.html", data)


def modificar_reserva(request, id):
    
    reserv = get_object_or_404(reserva, id=id)
    print(reserv)
    print(f"el id que se mando es es:{id}")
    data = {
        'form': formulario_reserva(instance=reserv)
    }
    if request.method == "POST":
        formulario = formulario_reserva(data=request.POST, instance=reserv, files=request.FILES)
        print(formulario)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="inicio")
        data['form']=formulario

    return render(request, "modificar_reserva.html", data)

def elimina_reserva(request, id):
    reserv = get_object_or_404(reserva, id=id)
    reserv.delete()
    return redirect(to='inicio')

def lista_habit(request):
    habit = habitacion.objects.all()
    cant = habitacion.objects.count()
    data = {"habit":habit,"Cantidad":cant}
    return render(request, "listar_habitaciones.html", data)

def elimina_habit(request, id):
    reserv = get_object_or_404(habitacion, id=id)
    reserv.delete()
    return redirect(to='inicio')

