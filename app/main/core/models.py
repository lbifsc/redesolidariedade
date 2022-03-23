from django.core.validators import RegexValidator, MinLengthValidator
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from cpf_field.models import CPFField
from django_cpf_cnpj.fields import CNPJField

PAPEL_CHOICES = (
    ('a', 'Admin'),
    ('b', 'User')
)

class Entidade(models.Model):
    cnpj = CNPJField('cnpj')
    telefone = models.CharField(max_length=24)
    nome = models.CharField(max_length=96)
    email = models.EmailField('email')
    endereco = models.CharField(max_length=96)
    data_cadastro = models.DateField(auto_now_add=True, verbose_name='data de cadastro')

    def __str__(self):
        return self.nome

class Representante(models.Model):
    idEntidade = models.ForeignKey(Entidade, on_delete=models.CASCADE, blank = True, null = True)
    nome = models.CharField(max_length=96)
    cpf = CPFField('cpf')
    endereco = models.CharField(max_length=96)
    observacao = models.TextField(max_length=96, blank = True, null = True)
    data_cadastro = models.DateField(auto_now_add=True, verbose_name='data de cadastro')

    def __str__(self):
        return self.nome

class Familia(models.Model):
    nomeChefeFamilia = models.CharField(max_length=96)
    cpfChefeFamilia = CPFField('cpf')
    enderecoChefeFamilia = models.CharField(max_length=96)
    data_cadastro = models.DateField(auto_now_add=True, verbose_name='data de cadastro')

    def __str__(self):
        return self.nomeChefeFamilia

class IntegranteFamilia(models.Model):
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)
    nome = models.CharField(max_length=96)
    cpf = CPFField('cpf')
    data_cadastro = models.DateField(auto_now_add=True, verbose_name='data de cadastro')

    def __str__(self):
        return self.nome       

class CategoriaItem(models.Model):
    descricao = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.descricao

class Item(models.Model):
    descricao = models.CharField(max_length=100)
    categoria = models.ForeignKey(CategoriaItem, on_delete=models.CASCADE)
    data_cadastro = models.DateField(auto_now_add=True, verbose_name='data de cadastro')

    def __str__(self):
        return self.descricao

class Movimentos(models.Model):
    idFamilia = models.ForeignKey(Familia, on_delete=models.CASCADE)
    representante = models.ForeignKey(Representante, on_delete=models.CASCADE, blank = True, null = True)
    data = models.DateTimeField(auto_now_add=True)
    justificativa = models.TextField(max_length=96, blank = True, null = True)

    def __str__(self):
        return str("Movimento " + str({self.pk}))

class MovimentosItem(models.Model):
    movimentos = models.ForeignKey(Movimentos, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    data_cadastro = models.DateField(auto_now_add=True, verbose_name='data de cadastro')

    def __str__(self):
        return self.item.descricao