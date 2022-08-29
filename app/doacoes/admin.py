from django.contrib import admin
from . import models 

class MovimentosAdmin(admin.ModelAdmin):
    list_display = ('id','idFamilia','representante','data','justificativa')

admin.site.register(models.Movimentos, MovimentosAdmin)

class MovimentosItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'movimentos', 'item', 'quantidade', 'data_cadastro')

admin.site.register(models.MovimentosItem, MovimentosItemAdmin)
