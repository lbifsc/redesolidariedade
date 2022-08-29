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

#------------------------------------------------------------------------------