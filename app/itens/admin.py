from django.contrib import admin
from . import models

class CategoriaItemAdmin(admin.ModelAdmin):
    list_display = ('id','descricao')

admin.site.register(models.CategoriaItem, CategoriaItemAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id','categoria','descricao','data_cadastro')

admin.site.register(models.Item, ItemAdmin)