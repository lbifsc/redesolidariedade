from django.contrib import admin
from . import models

class EntidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'cnpj', 'telefone','nome', 'email', 'endereco', 'data_cadastro')

admin.site.register(models.Entidade, EntidadeAdmin)

class RepresentanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'idEntidade', 'nome','cpf', 'endereco', 'observacao', 'data_cadastro')

admin.site.register(models.Representante, RepresentanteAdmin)
