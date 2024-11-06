from django.db import models

class hotel (models.Model):
    nombre = models.CharField(max_length=30)
    ubucacion = models.CharField(max_length=50)
    calif = models.FloatField()
    def __str__(self):
        return f"Hotel -- nombre: {self.nombre} -- calificacion: {self.calif}"


class habitacion(models.Model):
    hotel = models.ForeignKey(hotel, on_delete = models.CASCADE)
    numero_hab = models.CharField(max_length=5)
    tipo_hab = models.CharField(max_length=20)
    prec_noch = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"Hotel: {self.hotel}-- Tipo: {self.tipo_hab} -- numero: {self.numero_hab} -- precio: {self.prec_noch}"


class reserva(models.Model):
    cuarto = models.ForeignKey(habitacion, on_delete= models.CASCADE)
    nombre_cliente = models.CharField(max_length=50)
    fech_entrada = models.DateField()
    fech_salida = models.DateField()
    precio_total = models.DecimalField(max_digits=7, decimal_places=2)
    reservado = models.BooleanField(default=False)

    def __str__(self):
        return f"Reserva-- nombre: {self.nombre_cliente} -- entrada: {self.fech_entrada} -- salida: {self.fech_salida}"
    

class servicio(models.Model):
    Estrellas = models.IntegerField()
    

