from django.urls import path
from itens import views

#------------------------------------------------------------------------------
# URLS ITENS 
#------------------------------------------------------------------------------

#CRUD CATEGORIA
urlpatterns = [
    path('listaCategoria/', views.listaCategoriaItem.as_view(), name='Lista de Categorias'),
    path('cadastroCategoriaItem/', views.cadastroCategoriaItem, name = 'Cadastro Categoria Item'),
    path('cadastroCategoriaItem/edit/<int:pk>/', views.editarCategoria, name='Editar Categoria'),
    path('cadastroCategoriaItem/delete/<int:pk>/', views.excluirCategoria, name='Excluir Categoria'),
]

#CRUD ITEM
urlpatterns += [
    path('listaItem/', views.listaItem.as_view(), name='Lista de Itens'),
    path('cadastroItem/', views.cadastroItem, name='Cadastro de Itens'),
    path('cadastroItem/edit/<int:pk>/', views.editarItem, name='Editar Item'),
    path('cadastroItem/delete/<int:pk>/', views.excluirItem, name='Excluir Item'),
]

#SEARCH
urlpatterns += [
    path('searchItemByName/', views.searchItemByName, name='searchItemByName'),
    path('searchCategoriaByName/', views.searchCategoriaByName, name='searchCategoriaByName'),
]

#------------------------------------------------------------------------------