from django import forms
from .models import Servicio,especialista,agendar

class ServicioForm(forms.ModelForm):

    class Meta:
        model = Servicio
        fields = '__all__'

class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = especialista
        fields = '__all__'

class AgendarForm(forms.ModelForm):
    class Meta:
        model = agendar
        fields = ['nombre', 'telefono', 'correo', 'mensaje', 'fecha', 'servicio', 'especialista']
