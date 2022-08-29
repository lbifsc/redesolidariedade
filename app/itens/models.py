from django.db import models

#------------------------------------------------------------------------------
# DATABASE ITEM
#------------------------------------------------------------------------------

#MODEL CATEGORIA DE ITEM
class CategoriaItem(models.Model):
    descricao = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.descricao
        
#MODEL ITEM
class Item(models.Model):
    categoria = models.ForeignKey(CategoriaItem, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    data_cadastro = models.DateField(auto_now_add=True, verbose_name='data de cadastro')

    def __str__(self):
        return self.descricao

#------------------------------------------------------------------------------