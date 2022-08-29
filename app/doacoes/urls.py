from django.urls import path
from doacoes import views

#------------------------------------------------------------------------------
#URLS DOACOES
#------------------------------------------------------------------------------

#CRUD DOACOES
urlpatterns = [
    path('listaDoacao/', views.listaDoacao.as_view(), name='Lista de Doações'),
    path('detalhesDoacao/<int:pk>/', views.detalhesDoacao, name='Detalhes Doação'),
    path('cadastroDoacao/', views.buscacpf, name='Cadastro de Doações'),
    path('realizaDoacao/<int:pk>/', views.movimentos, name='Realizar Doação'),
    path('cadastroDoacao/delete/<int:pk>/', views.excluirDoacao, name='Excluir Doação'),
]

#------------------------------------------------------------------------------