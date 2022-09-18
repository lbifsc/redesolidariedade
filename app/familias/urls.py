from django.urls import path
from familias import views

#------------------------------------------------------------------------------
#URLS FAMILIAS
#------------------------------------------------------------------------------

#CRUD FAMILIA
urlpatterns = [
    path('listaFamilia/', views.listaFamilia.as_view(), name='Lista de Familias'),
    path('detalhesFamilia/<int:pk>/', views.detalhesFamilia, name='Detalhes Familia'),
    path('cadastroFamilia/', views.cadastroFamilia, name='Cadastro de Famílias'),
    path('cadastroFamilia/edit/<int:pk>/', views.editarFamilia, name='Editar Familia'),
    path('cadastroFamilia/delete/<int:pk>/', views.excluirFamilia, name='Excluir Familia'),
]

#CRUD INTEGRANTE FAMILIA
urlpatterns += [
    path('cadastroIntegranteFamilia/', views.cadastroIntegranteFamilia, name='Cadastro de IntegranteFamilia'),
    path('cadastroIntegranteFamilia/edit/<int:pk>/', views.editarIntegranteFamilia, name='Editar IntegranteFamilia'),
    path('cadastroIntegranteFamilia/delete/<int:pk>/', views.excluirIntegranteFamilia, name='Excluir IntegranteFamilia'),
]

#------------------------------------------------------------------------------