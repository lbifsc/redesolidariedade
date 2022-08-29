from django import forms
from .models import CategoriaItem, Item

#------------------------------------------------------------------------------
#FORMULARIOS ITEM
#------------------------------------------------------------------------------

#FORMULARIO CATEGORIA DE ITEM
class CategoriaItemForm(forms.ModelForm):
    class Meta:
        model = CategoriaItem
        labels = {
          "descricao": "Descrição",
        }
        fields = "__all__"     

#FORMULARIO ITEM
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        labels = {
          "descricao": "Descrição",
          "categoria": "Categoria"
        }
        fields = "__all__"

#------------------------------------------------------------------------------
