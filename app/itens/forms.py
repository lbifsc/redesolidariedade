from django import forms
from .models import CategoriaItem, Item

#------------------------------------------------------------------------------
#FORMULARIOS ITEM
#------------------------------------------------------------------------------

#FORMULARIO CATEGORIA DE ITEM
class CategoriaItemForm(forms.ModelForm):
  
    def __init__(self, *args, **kwargs):
        super(CategoriaItemForm, self).__init__(*args, **kwargs)
        self.fields['descricao'].widget.attrs.update({'placeholder' : 'Descrição da categoria de itens', 'icone' : 'fa-info'})

    class Meta:
        model = CategoriaItem
        labels = {
          "descricao": "Descrição",
        }
        fields = "__all__"     

#FORMULARIO ITEM
class ItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
      super(ItemForm, self).__init__(*args, **kwargs)
      self.fields['categoria'].widget.attrs.update({'class':'select-input','placeholder' : 'Selecione a categoria do item', 'icone' : 'fa-search'})
      self.fields['descricao'].widget.attrs.update({'placeholder' : 'Descrição da categoria de itens', 'icone' : 'fa-info'})

    class Meta:
        model = Item
        labels = {
          "descricao": "Descrição",
          "categoria": "Categoria"
        }
        fields = "__all__"

#------------------------------------------------------------------------------
