import re
from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _

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


class RedefinirSenhaForm(forms.Form):
    novaSenha = forms.CharField(label = "Nova senha", required=True)
    novaSenhaConfirmacao = forms.CharField(label = "Confirmação da nova senha", required=True)