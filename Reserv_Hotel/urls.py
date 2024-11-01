from django.urls import path

from .views import (
    inicio,
    habitaciones,

)


urlpatterns = [
    path("inicio/", inicio, name="inicio" ),
    path("habitacion/", habitaciones, name="habitacion" ),
]
