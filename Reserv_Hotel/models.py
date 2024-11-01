from django.db import models

class hotel (models.Model):
    nombre = models.CharField(max_length=30)
    ubucacion = models.CharField(max_length=50)
    calif = models.FloatField()


class habitacion(models.Model):
    hotel = models.ForeignKey(hotel, on_delete = models.CASCADE)
    numero_hab = models.CharField(max_length=5)
    tipo_hab = models.CharField(max_length=20)
    prec_noch = models.DecimalField(max_digits=7, decimal_places=2)


class reserva(models.Model):
    cuarto = models.ForeignKey(habitacion, on_delete= models.CASCADE)
    nombre_cliente = models.CharField(max_length=50)
    fech_entrada = models.DateField()
    fech_salida = models.DateField()
    precio_total = models.DecimalField(max_digits=7, decimal_places=2)
    

class servicio(models.Model):
    Estrellas = models.IntegerField()
