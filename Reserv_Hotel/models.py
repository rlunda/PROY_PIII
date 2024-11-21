from django.db import models
import datetime

class hoteles(models.Model):
    nombre = models.CharField(max_length=30)
    ubucacion = models.CharField(max_length=50)
    calif = models.FloatField()
    def __str__(self):
        return f"nombre: {self.nombre} -- calificacion: {self.calif}"


class habitacion(models.Model):
    hotel = models.ForeignKey(hoteles, on_delete = models.CASCADE)
    numero_hab = models.CharField(max_length=5)
    tipo_hab = models.CharField(max_length=20)
    info = models.CharField(max_length=200)
    prec_noch = models.DecimalField(max_digits=7, decimal_places=2)
    ocupado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.hotel}-- Tipo: {self.tipo_hab} -- numero: {self.numero_hab} -- precio: {self.prec_noch}"


class reserva(models.Model):
    cuarto = models.ForeignKey(habitacion, on_delete= models.CASCADE)
    nombre_cliente = models.CharField(max_length=50)
    dni = models.IntegerField(max_length=8, unique=True, blank=False, null=False)
    fech_entrada = models.DateField(default=datetime.date.today)
    fech_salida = models.DateField(default=datetime.date.today)
    precio_total = models.DecimalField(max_digits=7, decimal_places=2)
    reservado = models.BooleanField(default=False)

    def __str__(self):
        return f"Reserva-- nombre: {self.nombre_cliente} -- entrada: {self.fech_entrada} -- salida: {self.fech_salida}"
    

class servicio(models.Model):
    Estrellas = models.IntegerField()

class cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField(max_length=8, unique=True, blank=False, null=False)
    email = models.CharField(max_length=30)
    telefono = models.IntegerField(max_length=8, unique=True, blank=False, null=False)
    def __str__(self):
        return f"nombre: {self.nombre} -- dni:{self.dni}"
    
