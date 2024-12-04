from django import forms
from .models import reserva, hoteles, habitacion #modelos de la app
from django.contrib.auth.forms import UserCreationForm #esta herramienta nos ayuda a resguardar datos del login
from django.contrib.auth.models import User # importamos el modelo user para usarlo en el login

class formulario_reserva(forms.ModelForm):
    class Meta():
        model = reserva
        fields = ['cuarto','Cliente', 'dni', 'telefono','fech_entrada','fech_salida','precio_total','reservado']

class formulario_hotel(forms.ModelForm):
    imagen =forms.ImageField(required=False)
    class Meta():
        model = hoteles
        fields = '__all__'

class form_habitacion(forms.ModelForm):
    imagen =forms.ImageField(required=False)
    class Meta():
        model = habitacion
        fields = '__all__'

class customusercreateform(UserCreationForm):
    class Meta():
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']