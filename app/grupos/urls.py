from django.urls import path
from grupos import views

#------------------------------------------------------------------------------
#URLS GRUPOS
#------------------------------------------------------------------------------

#CRUD ENTIDADE
urlpatterns = [
    path('listaEntidades/', views.listaEntidades.as_view(), name='Lista de Entidades'),
    path('detalhesEntidade/<int:pk>/', views.detalhesEntidade.as_view(), name='Detalhes Entidade'),
    path('cadastroEntidade/', views.cadastroEntidade, name='Cadastro de Entidades'),
    path('cadastroEntidade/edit/<int:pk>/', views.editarEntidade, name='Editar Entidade'),
    path('cadastroEntidade/delete/<int:pk>/', views.excluirEntidade, name='Excluir Entidade'),
]

#CRUD REPRESENTANTES
urlpatterns += [
    path('listaRepresentante/', views.listaRepresentante.as_view(), name='Lista de Representantes'),
    path('detalhesRepresentante/<int:pk>/', views.detalhesRepresentante.as_view(), name='Detalhes Representante'),
    path('cadastroRepresentante/', views.cadastroRepresentante, name='Cadastro de Representantes'),
    path('cadastroRepresentante/edit/<int:pk>/', views.editarRepresentante, name='Editar Representante'),
    path('cadastroRepresentante/delete/<int:pk>/', views.excluirRepresentante, name='Excluir Representante'),
]

#CRUD USUARIOS
urlpatterns += [
    path('listaUsuario/', views.listaUsuario.as_view(), name='Lista de Usuarios'),
    path('cadastroUsuario/delete/<int:pk>/', views.excluirUsuario, name='Excluir Usuario'),
    path('redefinirSenha/', views.redefinirSenha, name='Redefinir Senha'),
    path('redefinicaoSenhaCompleta/', views.redefinicaoSenhaCompleta, name='Redefinição de Senha Completa'),
]

#SEARCH
urlpatterns += [
    path('searchEntidadeByName/', views.searchEntidadeByName, name='searchEntidadeByName'),
    path('searchRepresentanteByName/', views.searchRepresentanteByName, name='searchRepresentanteByName'),
]

#------------------------------------------------------------------------------