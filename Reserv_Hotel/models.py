from django.db import models
import datetime

class hoteles(models.Model):
    nombre = models.CharField(max_length=30)
    ubucacion = models.CharField(max_length=50)
    calif = models.FloatField()
    imagen = models.ImageField(upload_to="productos", null=False)
    def __str__(self):
        return f"nombre: {self.nombre} -- calificacion: {self.calif}"

clase_hab = [
    [0, "Doble"],
    [1, "Triple"],
    [2, "Cuadruple"],
    [3, "Familar"],
    [4, "Matrimonial"],
    [5, "Pen house"]

]

class habitacion(models.Model):
    hotel = models.ForeignKey(hoteles, on_delete = models.CASCADE)
    numero_hab = models.CharField(max_length=5)
    tipo_hab = models.IntegerField(choices=clase_hab)
    info = models.CharField(max_length=200)
    prec_noch = models.DecimalField(max_digits=7, decimal_places=2)
    ocupado = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return f"{self.hotel.nombre}-- Tipo: {self.tipo_hab} -- numero: {self.numero_hab} -- precio: {self.prec_noch}"



class reserva(models.Model):
    cuarto = models.ForeignKey(habitacion, on_delete= models.CASCADE)

    Cliente = models.IntegerField() #aqui hay que poner los los mismos datos que figuran en el modelo use, tambien el dni para luego buscarlo con este, 
    #el cliente deve ser remplasado por la lista de users, tambien se lo podria buscar por el id del user
    dni = models.IntegerField()
    telefono = models.IntegerField()
    fech_entrada = models.DateField(default=datetime.date.today)
    fech_salida = models.DateField(default=datetime.date.today)
    precio_total = models.DecimalField(max_digits=7, decimal_places=2)
    reservado = models.BooleanField(default=False)
    servicios = models.CharField(max_length=20)

    def __str__(self):
        return f" cliente: {self.Cliente}-- entrada: {self.fech_entrada} -- salida: {self.fech_salida}"
    

class servicio(models.Model):
    mascotas= models.BooleanField(default=False)
