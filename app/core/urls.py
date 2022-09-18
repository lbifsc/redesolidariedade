from core import views
from django.urls import path
from django.conf.urls import include

#------------------------------------------------------------------------------
#URLS CORE
#------------------------------------------------------------------------------

#INDEX
urlpatterns = [
    path('home/', views.home, name='Rede Solidariedade'),
]

#MODULOS
urlpatterns += [
    path('doacoes/', include('doacoes.urls')),
    path('familias/', include('familias.urls')),
    path('grupos/', include('grupos.urls')),
    path('itens/', include('itens.urls')),
    path('relatorios/', include('relatorios.urls')),
]

#SEARCH
urlpatterns += [
    path('searchFamiliaByName/', views.searchFamiliaByName, name='searchFamiliaByName'),
    path('searchFamiliaByCpf/', views.searchFamiliaByCpf, name='searchFamiliaByCpf'), 
    path('searchEntidadeByName/', views.searchEntidadeByName, name='searchEntidadeByName'),
    path('searchRepresentanteByName/', views.searchRepresentanteByName, name='searchRepresentanteByName'),
    path('searchItemByName/', views.searchItemByName, name='searchItemByName'),
    path('searchCategoriaByName/', views.searchCategoriaByName, name='searchCategoriaByName'),
]

#------------------------------------------------------------------------------