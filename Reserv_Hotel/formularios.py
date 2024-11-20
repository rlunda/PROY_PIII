from django import forms
from .models import reserva, hoteles


class formulario_reserva(forms.ModelForm):
    class Meta():
        model = reserva
        fields = ['cuarto','nombre_cliente','fech_entrada','fech_salida','precio_total','reservado']

class formulario_hotel(forms.ModelForm):
    class Meta():
        model = hoteles
        fields = ['nombre','ubucacion','calif']
