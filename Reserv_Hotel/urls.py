from django.urls import path

from .views import (
    index,
    habitaciones,
    about,
    inicio,
    disponibles,

)


urlpatterns = [
    path("index/", index, name="index" ),
    path("inicio", inicio, name ="inicio"),
    path("habitacion/", habitaciones, name="habitacion" ),
    path("about/", about, name="about"),
    path("disponibles/", disponibles, name="disponibles"),
]
