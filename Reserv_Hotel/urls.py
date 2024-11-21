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
)


urlpatterns = [
    path("inicio/", habitaciones, name="inicio" ),
    path("habitacion/", habitaciones, name="habitacion" ),
    path("HOTELES/", Hoteles, name="Hoteles"),
    path("reservados/", reservadoss, name="disponibles"),
    path("reserva_nuevo/", form_reserva, name = "reservanuevo"),
    path("nuevo_hotel/", form_hotel, name="nuevohotel"),
    path("Soport/",soporte, name = "Soportes"),
    path("informacion/", information, name = "informacion")

]
