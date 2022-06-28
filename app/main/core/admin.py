from django.contrib import admin

from . import models

class EntidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'cnpj', 'telefone','nome', 'email', 'endereco', 'data_cadastro')

admin.site.register(models.Entidade, EntidadeAdmin)

class RepresentanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'idEntidade', 'nome','cpf', 'endereco', 'observacao', 'data_cadastro')

admin.site.register(models.Representante, RepresentanteAdmin)

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('id','nomeChefeFamilia','cpfChefeFamilia','enderecoChefeFamilia','data_cadastro')

admin.site.register(models.Familia, FamiliaAdmin)

class IntegranteFamiliaAdmin(admin.ModelAdmin):
    list_display = ('id','familia','nome','cpf','data_cadastro')

admin.site.register(models.IntegranteFamilia, IntegranteFamiliaAdmin)

class CategoriaItemAdmin(admin.ModelAdmin):
    list_display = ('id','descricao')

admin.site.register(models.CategoriaItem, CategoriaItemAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id','categoria','descricao','data_cadastro')

admin.site.register(models.Item, ItemAdmin)

class MovimentosAdmin(admin.ModelAdmin):
    list_display = ('id','idFamilia','representante','data','justificativa')

admin.site.register(models.Movimentos, MovimentosAdmin)

class MovimentosItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'movimentos', 'item', 'quantidade', 'data_cadastro')

admin.site.register(models.MovimentosItem, MovimentosItemAdmin)