from django import forms
from .models import reserva, hoteles, habitacion


class formulario_reserva(forms.ModelForm):
    class Meta():
        model = reserva
        fields = ['cuarto','Cliente','fech_entrada','fech_salida','precio_total','reservado']

class formulario_hotel(forms.ModelForm):
    class Meta():
        model = hoteles
        fields = ['nombre','ubucacion','calif']

class form_buequeda(forms.Form):
    dni = forms.IntegerField()

class form_habitacion(forms.ModelForm):
    class Meta():
        model = habitacion
        fields = ['hotel', 'numero_hab', 'tipo_hab', 'info', 'prec_noch', 'ocupado']

