from django.urls import path

from .views import (
    inicio,
    habitaciones,
    Hoteles,
    reservadoss,
    form_reserva,
    form_hotel,
    soporte,
    information,
    #busca_dni,
    #buscado_dni,
    nueva_habit,
)


urlpatterns = [
    path("inicio", inicio, name="inicio"),
    path("inicio/", habitaciones, name="inicio" ),# paguina de inicio
    path("habitacion/", habitaciones, name="habitacion" ),# lista de habitaciones disponibles
    path("HOTELES/", Hoteles, name="Hoteles"),# Lista de hoteles existentes
    path("reservados/", reservadoss, name="disponibles"),# Lista todas las reservas que se Hicieron
    path("reserva_nuevo/", form_reserva, name = "reservanuevo"),# formulario nueva reserva
    path("nuevo_hotel/", form_hotel, name="nuevohotel"),# formulario agrega hotel
    path("Soport/",soporte, name = "Soportes"),# Pestania de soporte y configuraciones
    path("informacion/", information, name = "informacion"),# Pestania de informacion de pagina
  #  path("buscar/", busca_dni, name = "buscadni"),# formulario de busqueda dni
 #   path("buscado/", buscado_dni, name = "buscadodni"),#
    path("nueva-habit/", nueva_habit, name= "nueva_habit"),

]
