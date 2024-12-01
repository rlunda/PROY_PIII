from django.contrib import admin

# Register your models here.
from .models import hoteles,habitacion,cliente,reserva
# Register your models here.

admin.site.register(hoteles)
admin.site.register(habitacion)
admin.site.register(reserva)
admin.site.register(cliente)