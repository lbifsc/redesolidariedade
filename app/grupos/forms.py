from django import forms
from django.utils.translation import gettext as _
from .models import Entidade, Representante

#------------------------------------------------------------------------------
#FORMULARIOS REPRESENTANTES
#------------------------------------------------------------------------------

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
          "endereco": "Endereço",
          "observacao": "Observação"
        }
        fields = "__all__"
        exclude = ['cpf']

#------------------------------------------------------------------------------
#FORMULARIOS USUARIOS
#------------------------------------------------------------------------------

#FORMULARIO REDEFINICAO DE SENHA
class RedefinirSenhaForm(forms.Form):
    novaSenha = forms.CharField(label = "Nova senha", required=True)
    novaSenhaConfirmacao = forms.CharField(label = "Confirmação da nova senha", required=True)

#------------------------------------------------------------------------------