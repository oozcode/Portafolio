from django import forms
from .models import Servicio

class ServicioForm(forms.ModelForm):

    class Meta:
        model = Servicio
        fields = '__all__'
