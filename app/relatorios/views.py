from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from familias.models import Familia
from itens.models import Item
from doacoes.models import Movimentos

#------------------------------------------------------------------------------
# VIEWS RELATORIOS
#------------------------------------------------------------------------------

#RELATORIO DE DOACOES
class listaDoacaoRelatorio(LoginRequiredMixin, ListView):
    model = Movimentos
    template_name = 'relatorios/listaDoacaoRelatorio.html'
    context_object_name = 'doacoes'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

#RELATORIO DE FAMILIAS
class listaFamiliaRelatorio(LoginRequiredMixin, ListView):
    model = Familia
    template_name = 'relatorios/listaFamiliaRelatorio.html'
    context_object_name = 'familias'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

#RELATORIO DE ITENS
class listaItemRelatorio(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'relatorios/listaItemRelatorio.html'
    context_object_name = 'itens'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

#------------------------------------------------------------------------------
