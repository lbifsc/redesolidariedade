from django import forms
from django.utils.translation import gettext as _
from .models import Entidade, Representante

#------------------------------------------------------------------------------
#FORMULARIOS REPRESENTANTES
#------------------------------------------------------------------------------

class EntidadeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EntidadeForm, self).__init__(*args, **kwargs)
        self.fields['cnpj'].widget.attrs.update({'class':'select-input','placeholder' : 'CNPJ da entidade', 'icone' : 'fa-address-card'})  
        self.fields['nome'].widget.attrs.update({'class':'select-input','placeholder' : 'Nome da entidade', 'icone' : 'fa-user'})  
        self.fields['telefone'].widget.attrs.update({'class':'select-input','placeholder' : 'Telefone da entidade', 'icone' : 'fa-phone'})  
        self.fields['email'].widget.attrs.update({'class':'select-input','placeholder' : 'E-mail da entidade', 'icone' : 'fa-envelope'})  
        self.fields['endereco'].widget.attrs.update({'class':'select-input','placeholder' : 'Endereço da entidade', 'icone' : 'fa-home'})  


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
    novaSenha = forms.CharField(label = "Nova senha", required=True)
    senhaAtual = forms.CharField(label = "Senha atual", required=True)
#------------------------------------------------------------------------------
