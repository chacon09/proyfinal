from django import forms

from .models import Deportista, Deporte


class DeportistaForm(forms.ModelForm):
#todos los campos de Pelicula
   class Meta:
      model = Deportista
      fields = ('nombre', 'edad', 'deportes')
def __init__ (self, *args, **kwargs):
     super(DeportistaForm, self).__init__(*args, **kwargs)

     self.fields["deporte"].widget = forms.widgets.CheckboxSelectMultiple()

     self.fields["deporte"].help_text = "Ingrese los deportes a practicar"

     self.fields["deporte"].queryset = Deporte.objects.all()

class DeporteForm(forms.ModelForm):
    class Meta:
        model = Deporte
        fields = ('nombre', 'descripcion')
