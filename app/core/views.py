
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import date, timedelta
from familias.models import Familia
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