from django.db import models
from django_cpf_cnpj.fields import CNPJField, CPFField

#------------------------------------------------------------------------------
# DATABASE FAMILIAS
#------------------------------------------------------------------------------

#MODEL FAMILIAS
class Familia(models.Model):
    nomeChefeFamilia = models.CharField(max_length=96)
    cpfChefeFamilia = CPFField(masked=False)
    enderecoChefeFamilia = models.CharField(max_length=96)
    data_cadastro = models.DateField(auto_now_add=True, verbose_name='data de cadastro')

    def __str__(self):
        return self.nomeChefeFamilia

#MODEL INTEGRANTES DE FAMILIA
class IntegranteFamilia(models.Model):
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)
    nome = models.CharField(max_length=96)
    cpf = CPFField(masked=False)
    data_cadastro = models.DateField(auto_now_add=True, verbose_name='data de cadastro')

    def __str__(self):
        return self.nome  

#------------------------------------------------------------------------------