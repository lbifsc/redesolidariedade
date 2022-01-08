from django.db.models.fields import CharField, EmailField, TextField
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from types import NoneType

PAPEL_CHOICES = (
    ('a', 'Admin'),
    ('b', 'User')
)

CATEGORIA_CHOICES = (
    ('1', 'Alimento Não Perecível'),
    ('2', 'Remédio'),
    ('3', 'Protetor Solar')
)

class Entidade(models.Model):
    cnpj = models.CharField(max_length=24, blank = True, null = True)
    nome = models.CharField(max_length=96, blank = True, null = True)
    telefone = models.CharField(max_length=24, blank = True, null = True)
    email = models.EmailField(blank = True, null = True)
    endereco = models.CharField(max_length=96, blank = True, null = True)

    def __str__(self):
        return self.nome

class Representante(models.Model):
    idEntidade = models.ForeignKey(Entidade, on_delete=models.CASCADE, blank = True, null = True)
    nome = models.CharField(max_length=96, blank = True, null = True)
    cpf = models.CharField(max_length=24, blank = True, null = True)
    endereco = models.CharField(max_length=96, blank = True, null = True)
    obsercacao = models.TextField(max_length=96, blank = True, null = True)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    usuario = models.CharField(max_length=100, blank = True, null = True)
    senha = models.CharField(max_length=100, blank = True, null = True)
    representante = models.ForeignKey(Representante, on_delete=models.CASCADE, blank = True, null = True)
    papel = models.CharField(choices=PAPEL_CHOICES, max_length=2, blank = True, null = True)

    def __str__(self):
        return self.usuario

class Familia(models.Model):
    nomeChefeFamilia = models.CharField(max_length=96, blank = True, null = True)
    cpfChefeFamilia = models.CharField(max_length=24, blank = True, null = True)
    enderecoChefeFamilia = models.CharField(max_length=96, blank = True, null = True)

    def __str__(self):
        return self.nomeChefeFamilia

class IntegranteFamilia(models.Model):
    Familia = models.ForeignKey(Familia, on_delete=models.CASCADE)
    nome = models.CharField(max_length=96, blank = True, null = True)
    cpf = models.CharField(max_length=24, blank = True, null = True)

    def __str__(self):
        return self.nome       

class Item(models.Model):
    descricao = models.CharField(max_length=100, blank = True, null = True)
    categoria = models.CharField(choices=CATEGORIA_CHOICES, max_length=50, blank = True, null = True)

    def __str__(self):
        return self.descricao

class Movimentos(models.Model):
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank = True, null = True)
    idFamilia = models.ForeignKey(Familia, on_delete=models.CASCADE, blank = True, null = True)
    data = models.DateTimeField(auto_now_add=True, blank = True, null = True)
    justificativa = models.TextField(max_length=96, blank = True, null = True)

    def __str__(self):
        return self.pk

class MovimentosItem(models.Model):
    movimentos = models.ForeignKey(Movimentos, on_delete=models.CASCADE, blank = True, null = True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank = True, null = True)
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.descricao}"