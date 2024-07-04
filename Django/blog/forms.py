from django import forms
from .models import Servicio,especialista

class ServicioForm(forms.ModelForm):

    class Meta:
        model = Servicio
        fields = '__all__'

class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = especialista
        fields = '__all__'
