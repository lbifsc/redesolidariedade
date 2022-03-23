import re
from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _
from .models import *

class EntidadeForm(forms.ModelForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if Entidade.objects.filter(email = email).exists():
            raise forms.ValidationError(_('Email já cadastrado.'))
        return email

    class Meta:
        model = Entidade
        labels = {
          "cnpj": "CNPJ",
          "nome": "Nome",
          "telefone": "Telefone",
          "email": "Email",
          "endereco": "Endereço"
        }
        fields = "__all__"

class RepresentanteForm(forms.ModelForm):
    class Meta:
        model = Representante
        labels = {
          "idEntidade": "Entidade",
          "nome": "Nome",
          "cpf": "CPF",
          "endereco": "Endereço",
          "observacao": "Observação"
        }
        fields = "__all__"

class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=96)

    def clean_email(self):
        email = self.cleaned_data['email']
        return email

    class Meta:
        model = User
        labels = {
          "username": "Nome de usuário",
          "email": "Email",
          "password1": "Senha"
        }
        fields = ['username', 'email', 'password1']

class FamiliaForm(forms.ModelForm):

    def clean_cpfChefeFamilia(self):
        cpfChefeFamilia = self.cleaned_data['cpfChefeFamilia']
        cpfChefeFamilia = re.sub('[^0-9]', '', cpfChefeFamilia)
        return cpfChefeFamilia

    class Meta:
        model = Familia
        labels = {
          "nomeChefeFamilia": "Nome do chefe da família",
          "cpfChefeFamilia": "CPF do chefe da família",
          "enderecoChefeFamilia": "Endereço",
        }
        fields = "__all__"

class IntegranteFamiliaForm(forms.ModelForm):

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        cpf = re.sub('[^0-9]', '', cpf)
        return cpf

    class Meta:
        model = IntegranteFamilia
        labels = {
          "familia": "Família de",
          "nome": "Nome",
          "cpf": "CPF"
        }
        fields = "__all__"

class CategoriaItemForm(forms.ModelForm):
    class Meta:
        model = CategoriaItem
        labels = {
          "descricao": "Descrição",
        }
        fields = "__all__"        

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        labels = {
          "descricao": "Descrição",
          "categoria": "Categoria"
        }
        fields = "__all__"

class MovimentosForm(forms.ModelForm):
    class Meta:
        model = Movimentos
        labels = {
          "idFamilia": "Código da família",
          "data": "Data da doação"
        }
        exclude = ['idFamilia', 'data']

class MovimentosItemForm(forms.ModelForm):
    class Meta:
        model = MovimentosItem
        exclude = ['movimentos']