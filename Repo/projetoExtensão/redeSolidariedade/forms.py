from django import forms

from .models import *

class EntidadeForm(forms.ModelForm):
    class Meta:
        model = Entidade
        fields = "__all__"

class RepresentanteForm(forms.ModelForm):
    class Meta:
        model = Representante
        fields = "__all__"

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"

class FamiliaForm(forms.ModelForm):
    class Meta:
        model = Familia
        fields = "__all__"

class IntegranteFamiliaForm(forms.ModelForm):
    class Meta:
        model = IntegranteFamilia
        fields = "__all__"

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"

