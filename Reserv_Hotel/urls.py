from django.urls import path
from django.contrib.auth import views as auth_views

from django.contrib.auth.views import LogoutView


from .views import (
    inicio,
    habitaciones,
    Hoteles,
    reservadoss,
    form_reserva,
    form_hotel,
    soporte,
    information,
    nueva_habit,
    registro,
    modificar_reserva,
    elimina_reserva,
    lista_habit,
    elimina_habit,
)


urlpatterns = [
    path("", inicio, name="inicio"),
    #path("inicio", inicio, name="inicio"),
    path("inicio/", habitaciones, name="inicio" ),# Paguina de inicio
    path("habitacion/", habitaciones, name="habitacion" ),# Lista de habitaciones disponibles
    path("HOTELES/", Hoteles, name="Hoteles"),# Lista de hoteles existentes
    path("reservados/", reservadoss, name="disponibles"),# Lista todas las reservas que se Hicieron
    path("reserva_nuevo/", form_reserva, name = "reservanuevo"),# Formulario nueva reserva
    path("nuevo_hotel/", form_hotel, name="nuevohotel"),# Formulario agrega hotel
    path("Soport/", soporte, name = "Soportes"),# Pestania de soporte y configuraciones
    path("informacion/", information, name = "informacion"),# Pestania de informacion de pagina
    path("nueva-habit/", nueva_habit, name= "nueva_habit"), # ingresa una nueva habitacion
    path("registro/",registro, name="registro"),# form para registrar un usuario
    path('Logout/', LogoutView.as_view(template_name='logout_tem.html'), name="Logout"), #LOGIN 
    path("modifica_reserva/<id>", modificar_reserva, name = "modificareserva"), 
    path("Elimina_reserva/<id>", elimina_reserva, name ="eliminareserva"),
    path("lista-habitaciones/", lista_habit, name="listarhabitaciones"),
    path("Elimina_habit/<id>", elimina_habit, name ="eliminahabit"),
    
]
