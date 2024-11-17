from django.urls import path

from .views import (
    inicio,
    habitaciones,
    about,
    inicio1,
    disponibles,
    form_reserva,

)


urlpatterns = [
    path("inicio/", inicio, name="inicio" ),
    path("inicio1", inicio1, name ="inicio1"),
    path("habitacion/", habitaciones, name="habitacion" ),
    path("about/", about, name="about"),
    path("reservados/", disponibles, name="disponibles"),
    path("reserva_nuevo/", form_reserva, name = "reservanuevo")

]
  