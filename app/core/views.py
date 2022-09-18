
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import date, timedelta
from familias.models import Familia, IntegranteFamilia
from grupos.models import Entidade, Representante
from itens.models import Item, CategoriaItem
from django.http import JsonResponse
from django.db.models import Q
from grupos.models import Entidade
from doacoes.models import Movimentos

#------------------------------------------------------------------------------
#VIEWS CORE
#------------------------------------------------------------------------------
@login_required
def home(request):
    families = Familia.objects.all()
    entities = Entidade.objects.all()
    donations = Movimentos.objects.all()

    end = date.today().replace(day=1) - timedelta(days=1)
    start = date.today().replace(day=1) - timedelta(days=end.day)

    today = date.today()
    yesterday = date.today() - timedelta(days=1)
    twodaysbefore = date.today() - timedelta(days=2)
    threedaysbefore = date.today() - timedelta(days=3)
    fourdaysbefore = date.today() - timedelta(days=4)
    fivedaysbefore = date.today() - timedelta(days=5)
    sixdaysbefore = date.today() - timedelta(days=6)
    last_week = date.today() - timedelta(days=7)

    chart_data = {


      'families': {
        'today': families.filter(data_cadastro__contains=today).count(),
        'yesterday': families.filter(data_cadastro__contains=yesterday).count(),
        'twodaysbefore': families.filter(data_cadastro__contains=twodaysbefore).count(),
        'threedaysbefore': families.filter(data_cadastro__contains=threedaysbefore).count(),
        'fourdaysbefore': families.filter(data_cadastro__contains=fourdaysbefore).count(),
        'fivedaysbefore': families.filter(data_cadastro__contains=fivedaysbefore).count(),
        'sixdaysbefore': families.filter(data_cadastro__contains=sixdaysbefore).count(),
        'last_week': families.filter(data_cadastro__contains=last_week).count(),
      },

      'entities': {
        'today': entities.filter(data_cadastro__contains=today).count(),
        'yesterday': entities.filter(data_cadastro__contains=yesterday).count(),
        'twodaysbefore': entities.filter(data_cadastro__contains=twodaysbefore).count(),
        'threedaysbefore': entities.filter(data_cadastro__contains=threedaysbefore).count(),
        'fourdaysbefore': entities.filter(data_cadastro__contains=fourdaysbefore).count(),
        'fivedaysbefore': entities.filter(data_cadastro__contains=fivedaysbefore).count(),
        'sixdaysbefore': entities.filter(data_cadastro__contains=sixdaysbefore).count(),
        'last_week': entities.filter(data_cadastro__contains=last_week).count(),
      },

      'donations': {
        'today': donations.filter(data__contains=today).count(),
        'yesterday': donations.filter(data__contains=yesterday).count(),
        'twodaysbefore': donations.filter(data__contains=twodaysbefore).count(),
        'threedaysbefore': donations.filter(data__contains=threedaysbefore).count(),
        'fourdaysbefore': donations.filter(data__contains=fourdaysbefore).count(),
        'fivedaysbefore': donations.filter(data__contains=fivedaysbefore).count(),
        'sixdaysbefore': donations.filter(data__contains=sixdaysbefore).count(),
        'last_week': donations.filter(data__contains=last_week).count(),
      }
    }

    context = {
      'family_count': families.count,
      'family_lastmonth': families.filter(data_cadastro__range=[start, end]).count(),
      'entity_count': entities.count,
      'entity_lastmonth': entities.filter(data_cadastro__range=[start, end]).count(),
      'donation_count': donations.count,
      'donation_lastmonth': donations.filter(data__range=[start, end]).count(),
      'chart_data': chart_data,
    }

    return render(request, 'generic/home.html', context)

#------------------------------------------------------------------------------
#SEARCH
#------------------------------------------------------------------------------

#FAMILIA POR NOME
def searchFamiliaByName(request):
    nome = request.GET.get('nomeChefeFamilia')
    payload=[]

    if nome:
        familias = Familia.objects.filter(
                Q(nomeChefeFamilia__icontains=nome) |
                Q(cpfChefeFamilia__icontains=nome)
            )

        for familia in familias:
            payload.append(familia.nomeChefeFamilia + ' -- CPF:' + str(familia.cpfChefeFamilia))

    return JsonResponse({'status': 200, 'data': payload})

#FAMILIA POR CPF
def searchFamiliaByCpf(request):
    cpf = request.GET.get('cpfChefeFamilia')
    payload=[]

    if cpf:
        membros = IntegranteFamilia.objects.filter(
                Q(nome__icontains=cpf)|
                Q(cpf__icontains=cpf)
            )
        familia = Familia.objects.filter(
                Q(nomeChefeFamilia__icontains=cpf)|
                Q(cpfChefeFamilia__icontains=cpf)
            )

        for integrante in membros:
            payload.append(integrante.nome + ' -- CPF:' + str(integrante.cpf))
        for chefe in familia:
            payload.append(chefe.nomeChefeFamilia + ' -- CPF:' + str(chefe.cpfChefeFamilia))

    return JsonResponse({'status': 200, 'data': payload})

#ENTIDADE POR NOME
def searchEntidadeByName(request):
    nomeEntidade = request.GET.get('nomeEntidade')
    payload=[]

    if nomeEntidade:
        entidades = Entidade.objects.filter(nome__icontains=nomeEntidade)

        for entidade in entidades:
            payload.append(entidade.nome)

    return JsonResponse({'status': 200, 'data': payload})

#REPRESENTANTE POR NOME
def searchRepresentanteByName(request):
    nomeRepresentante = request.GET.get('nomeRepresentante')
    payload=[]

    if nomeRepresentante:
        representantes = Representante.objects.filter(nome__icontains=nomeRepresentante)

        for representante in representantes:
            payload.append(representante.nome)

    return JsonResponse({'status': 200, 'data': payload})

#ITEM POR NOME
def searchItemByName(request):
    nomeItem = request.GET.get('nomeItem')
    payload=[]

    if nomeItem:
        itens = Item.objects.filter(descricao__icontains=nomeItem)

        for item in itens:
            payload.append(item.descricao)

    return JsonResponse({'status': 200, 'data': payload})

#CATEGORIA DE ITEM POR NOME
def searchCategoriaByName(request):
    nomeCategoria = request.GET.get('nomeCategoria')
    payload=[]

    if nomeCategoria:
        categorias = CategoriaItem.objects.filter(descricao__icontains=nomeCategoria)

        for categoria in categorias:
            payload.append(categoria.descricao)

    return JsonResponse({'status': 200, 'data': payload})

#------------------------------------------------------------------------------