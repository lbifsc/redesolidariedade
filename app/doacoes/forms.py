from django import forms
from .models import Movimentos

#------------------------------------------------------------------------------
#FORMULARIOS DOACOES
#------------------------------------------------------------------------------

#FORMULARIO DOACOES
class MovimentosForm(forms.ModelForm):
    class Meta:
        model = Movimentos
        labels = {
          "idFamilia": "Código da família",
          "data": "Data da doação"
        }
        exclude = ['idFamilia', 'data']

#------------------------------------------------------------------------------