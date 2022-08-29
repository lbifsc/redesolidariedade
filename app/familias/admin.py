from django.contrib import admin
from . import models

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('id','nomeChefeFamilia','cpfChefeFamilia','enderecoChefeFamilia','data_cadastro')

admin.site.register(models.Familia, FamiliaAdmin)

class IntegranteFamiliaAdmin(admin.ModelAdmin):
    list_display = ('id','familia','nome','cpf','data_cadastro')

admin.site.register(models.IntegranteFamilia, IntegranteFamiliaAdmin)