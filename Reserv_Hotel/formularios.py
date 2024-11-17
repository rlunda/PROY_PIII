from django import forms
from .models import reserva

class formulario_reserva(forms.Form):
    cliente = forms.CharField()
    dni = forms.IntegerField(max_value=12)
