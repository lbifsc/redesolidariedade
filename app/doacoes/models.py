from django.db import models
from itens.models import Item
from familias.models import Familia
from grupos.models import Representante

#------------------------------------------------------------------------------
# DATABASE MOVIMENTOS
#------------------------------------------------------------------------------

#MODEL MOVIMENTOS(DOACOES)
class Movimentos(models.Model):
    idFamilia = models.ForeignKey(Familia, on_delete=models.CASCADE)
    representante = models.ForeignKey(Representante, on_delete=models.CASCADE, blank = True, null = True)
    data = models.DateTimeField(auto_now_add=True)
    justificativa = models.TextField(max_length=96, blank = True, null = True)

    def __str__(self):
        return str("Movimento " + str({self.pk}))

#MODEL ITENS DE MOVIMENTO(ITENS DE DOACAO)
class MovimentosItem(models.Model):
    movimentos = models.ForeignKey(Movimentos, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    data_cadastro = models.DateField(auto_now_add=True, verbose_name='data de cadastro')

    def __str__(self):
        return self.item.descricao 

#------------------------------------------------------------------------------