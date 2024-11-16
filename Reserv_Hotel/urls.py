from django.urls import path

from .views import (
    inicio,
    habitaciones,
    Hoteles,
    inicio1,
    disponibles,

)


urlpatterns = [
    path("inicio/", inicio, name="inicio" ),
    path("inicio1", inicio1, name ="inicio1"),
    path("habitacion/", habitaciones, name="habitacion" ),
    path("HOTELES/", Hoteles, name="Hoteles"),
    path("reservados/", disponibles, name="disponibles"),
]
