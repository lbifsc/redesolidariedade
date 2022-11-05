from django.db import models
from django_cpf_cnpj.fields import CNPJField, CPFField

#------------------------------------------------------------------------------
# DATABASE REPRESENTANTES
#------------------------------------------------------------------------------

#MODEL ENTIDADE DE REPRESENTANTE
class Entidade(models.Model):
    cnpj = CNPJField(masked=False)
    telefone = models.CharField(max_length=24)
    nome = models.CharField(max_length=96, unique=True)
    email = models.EmailField('email')
    endereco = models.CharField(max_length=96)
    data_cadastro = models.DateField(auto_now_add=True, verbose_name='data de cadastro')

    def __str__(self):
        return self.nome


#MODEL REPRESENTANTES
class Representante(models.Model):
    idEntidade = models.ForeignKey(Entidade, on_delete=models.CASCADE, blank = True, null = True)
    nome = models.CharField(max_length=96, unique=True)
    cpf = CPFField(masked=False)
    endereco = models.CharField(max_length=96)
    observacao = models.TextField(max_length=96, blank = True, null = True)
    data_cadastro = models.DateField(auto_now_add=True, verbose_name='data de cadastro')

    def __str__(self):
        return self.nome

#------------------------------------------------------------------------------