from django.db import models


class habitacion(models.Model):
    nombre_hotel = models.CharField(max_length=30)
    Estrellas = models.IntegerField()
    piso = models.IntegerField()
    numero = models.CharField(max_length=5)
    codigo_hab = models.IntegerField()


# Create your models here.
