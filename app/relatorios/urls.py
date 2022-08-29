from django.urls import path
from relatorios import views

#------------------------------------------------------------------------------
# URLS RELATORIOS
#------------------------------------------------------------------------------

#RELATORIOS
urlpatterns = [
    path('listaDoacaoRelatorio/', views.listaDoacaoRelatorio.as_view(), name='listar_doacoes_relatorio'),
    path('listaFamiliaRelatorio/', views.listaFamiliaRelatorio.as_view(), name='listar_familias_relatorio'),
    path('listaItemRelatorio/', views.listaItemRelatorio.as_view(),name='listar_itens_relatorio'),
]

#------------------------------------------------------------------------------