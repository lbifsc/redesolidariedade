from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import *

class EntidadeForm(forms.ModelForm):
    class Meta:
        model = Entidade
        fields = "__all__"

class RepresentanteForm(forms.ModelForm):
    class Meta:
        model = Representante
        fields = "__all__"

class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=96)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

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

class MovimentosForm(forms.ModelForm):
    class Meta:
        model = Movimentos
        exclude = ['idFamilia', 'data']

class MovimentosItemForm(forms.ModelForm):
    class Meta:
        model = MovimentosItem
        exclude = ['movimentos']