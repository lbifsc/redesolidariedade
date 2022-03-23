from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.models import User 
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.views import generic
from datetime import date, timedelta
from django.contrib.auth.models import Group
from django.db.models import Q
from django.http import JsonResponse
import json

# Create your views here.

def cadastroDoacao(request):
    return render(request, 'cadastro.html')

def cadastroEntidade(request):
    form = EntidadeForm()
    if request.method == 'POST':
        form = EntidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista de Representantes')

    return render(request,'cadastro.html',{'form': form})

def cadastroFamilia(request):
    form = FamiliaForm()
    if request.method == 'POST':
        form = FamiliaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista de Familias')

    return render(request,'cadastro.html',{'form': form})

def cadastroIntegranteFamilia(request):
    if request.method == 'POST':
        novoIntegrante = IntegranteFamilia(
            familia= Familia.objects.get(cpfChefeFamilia=request.POST.get('idFamilia')),
            nome = request.POST.get('nomeIntegrante'),
            cpf= request.POST.get('cpfIntegrante')
        )

        novoIntegrante.save()
        return redirect('Lista de Familias')

    return render(request,'cadastroIntegranteFamiliar.html')

def cadastroCategoriaItem(request):
    form = CategoriaItemForm()
    if request.method == 'POST':
        form = CategoriaItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista de Categorias')

    return render(request,'cadastro.html',{'form': form})    

def cadastroItem(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista de Itens')

    return render(request,'cadastro.html',{'form': form})

def cadastroRepresentante(request):
    if request.method == 'POST':
        novoRepresentate = Representante(idEntidade = Entidade.objects.get(nome=request.POST.get('nomeEntidade')),
            nome = request.POST.get('nomeRepresentante'),
            cpf = request.POST.get('cpfRepresentate'),
            endereco = request.POST.get('endereco'),
            obsercacao = request.POST.get('observacao')
        )

        novoRepresentate.save()
        return redirect('Lista de Representantes')

    return render(request,'cadastroRepresentante.html')

def cadastroUsuario(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            created_user = form.save()
            created_user.groups.add(Group.objects.get(name='user_common'))
            return redirect('Lista de Usuarios')

    return render(request,'cadastro.html',{'form': form})

def editarDoacao(request):
    return render(request, 'cadastro.html')

def editarEntidade(request, pk, template_name='cadastro.html'):
    entidades = get_object_or_404(Entidade, pk=pk)
    form = EntidadeForm(request.POST or None, instance=entidades)
    if form.is_valid():
        form.save()
        return redirect('Lista de Representantes')
    return render(request, template_name, {'form':form})

def editarFamilia(request, pk, template_name='cadastro.html'):
    familias = get_object_or_404(Familia, pk=pk)
    form = FamiliaForm(request.POST or None, instance=familias)
    if form.is_valid():
        form.save()
        return redirect('Lista de Familias')
    return render(request, template_name, {'form':form})

def editarIntegranteFamilia(request, pk, template_name='cadastro.html'):
    integranteFamilia = get_object_or_404(IntegranteFamilia, pk=pk)
    form = IntegranteFamiliaForm(request.POST or None, instance=integranteFamilia)
    if form.is_valid():
        form.save()
        return redirect('Lista de Familias')
    return render(request, template_name, {'form':form})

def editarCategoria(request, pk, template_name='cadastro.html'):
    categoria = get_object_or_404(CategoriaItem, pk=pk)
    form = CategoriaItemForm(request.POST or None, instance=categoria)
    if form.is_valid():
        form.save()
        return redirect('Lista de Categorias')
    return render(request, template_name, {'form':form})    

def editarItem(request, pk, template_name='cadastro.html'):
    itens = get_object_or_404(Item, pk=pk)
    form = ItemForm(request.POST or None, instance=itens)
    if form.is_valid():
        form.save()
        return redirect('Lista de Itens')
    return render(request, template_name, {'form':form})

def editarRepresentante(request, pk, template_name='cadastro.html'):
    representantes = get_object_or_404(Representante, pk=pk)
    form = RepresentanteForm(request.POST or None, instance=representantes)
    if form.is_valid():
        form.save()
        return redirect('Lista de Representantes')
    return render(request, template_name, {'form':form})

def excluirCategoria(request, pk, template_name='confirm_delete.html'):
    categoria = get_object_or_404(CategoriaItem, pk=pk)
    if request.method=='POST':
        categoria.delete()
        return redirect('Lista de Categorias')
    return render(request, template_name, {'object':categoria})    

def excluirDoacao(request, pk, template_name='confirm_delete.html'):
    doacao = get_object_or_404(Movimentos, pk=pk)
    if request.method=='POST':
        doacao.delete()
        return redirect('Lista de Doações')
    return render(request, template_name, {'object':doacao})

def excluirEntidade(request, pk, template_name='confirm_delete.html'):
    entidade = get_object_or_404(Entidade, pk=pk)
    if request.method=='POST':
        entidade.delete()
        return redirect('Lista de Representantes')
    return render(request, template_name, {'object':entidade})

def excluirFamilia(request, pk, template_name='confirm_delete.html'):
    familia = get_object_or_404(Familia, pk=pk)
    if request.method=='POST':
        familia.delete()
        return redirect('Lista de Familias')
    return render(request, template_name, {'object':familia})

def excluirIntegranteFamilia(request, pk, template_name='confirm_delete.html'):
    integranteFamilia = get_object_or_404(IntegranteFamilia, pk=pk)
    if request.method=='POST':
        integranteFamilia.delete()
        return redirect('Lista de Familias')
    return render(request, template_name, {'object':integranteFamilia})

def excluirItem(request, pk, template_name='confirm_delete.html'):
    item = get_object_or_404(Item, pk=pk)
    if request.method=='POST':
        item.delete()
        return redirect('Lista de Itens')
    return render(request, template_name, {'object':item})

def excluirRepresentante(request, pk, template_name='confirm_delete.html'):
    representante = get_object_or_404(Representante, pk=pk)
    if request.method=='POST':
        representante.delete()
        return redirect('Lista de Representantes')
    return render(request, template_name, {'object':representante})

def excluirUsuario(request, pk, template_name='confirm_delete.html'):
    usuario = get_object_or_404(User, pk=pk)
    if request.method=='POST':
        usuario.delete()
        return redirect('Lista de Usuarios')
    return render(request, template_name, {'object':usuario})


def detalhesDoacao(request, pk):
    template_name = 'detalhesDoacao.html'
    movimento = Movimentos.objects.get(pk=pk)
    movimentosItens = MovimentosItem.objects.get_queryset().filter(movimentos=pk)
    context = {
        'movimento': movimento,
        'movimentosItens': movimentosItens,
    }
    return render(request, template_name, context)     

class detalhesEntidade(DetailView):
    model = Entidade
    template_name ='detalhesEntidade.html'


def detalhesFamilia(request, pk):
    template_name = 'detalhesFamilia.html'
    familia = Familia.objects.get(pk=pk)
    integrantesFamilia = IntegranteFamilia.objects.get_queryset().filter(familia=pk)
    context = {
        'familia': familia,
        'integrantesFamilia': integrantesFamilia,
    }
    return render(request, template_name, context)    

class detalhesRepresentante(DetailView):
    model = Representante
    template_name ='detalhesRepresentante.html'


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

    return render(request, 'home.html', context)

def relatorioDoacao(request):
    return render(request, 'relatorioDoacao.html')

def relatorioEntidade(request):
    return render(request, 'relatorioEntidade.html')

def relatorioFamilia(request):
    return render(request, 'relatorioFamilia.html')

def relatorioUsuario(request):
    return render(request, 'relatorioUsuario.html')

class listaDoacao(ListView):
    model = Movimentos
    template_name = 'listaDoacao.html'
    context_object_name = 'movimentos_list'

    def get_queryset(self):
        queryset = super(listaDoacao, self).get_queryset()
        data = self.request.GET
        search = data.get('search')
        if search:
            queryset = queryset.filter(
                Q(idFamilia__nomeChefeFamilia__icontains=search)
            )
        return queryset

class listaFamilia(ListView):
    model = Familia
    template_name = 'listaFamilia.html'
    context_object_name = 'familias_list'

    def get_queryset(self):
        queryset = super(listaFamilia, self).get_queryset()
        data = self.request.GET
        search = data.get('search')
        if search:
            queryset = queryset.filter(
                Q(nomeChefeFamilia__icontains=search) |
                Q(cpfChefeFamilia__icontains=search) |
                Q(enderecoChefeFamilia__icontains=search)
            )
        return queryset

class listaRepresentante(ListView):
    model = Representante
    template_name = 'listaRepresentante.html'
    context_object_name = 'representantes_list'

    def get_queryset(self):
        queryset = super(listaRepresentante, self).get_queryset()
        data = self.request.GET
        search = data.get('search')
        if search:
            queryset = queryset.filter(
                Q(nome__icontains=search) |
                Q(cpf__icontains=search) |
                Q(endereco__icontains=search)
            )
        return queryset

class listaUsuario(ListView):
    model = User
    template_name = 'listaUsuario.html'
    context_object_name = 'usuarios_list'

    def get_queryset(self):
        queryset = super(listaUsuario, self).get_queryset()
        data = self.request.GET
        search = data.get('search')
        if search:
            queryset = queryset.filter(
                Q(username__icontains=search)
            )
        return queryset

class listaCategoriaItem(ListView):
    model = CategoriaItem
    template_name = 'listaCategoria.html'
    context_object_name = 'categoriaItens_list'

    def get_queryset(self):
        queryset = super(listaCategoriaItem, self).get_queryset()
        data = self.request.GET
        search = data.get('search')
        if search:
            queryset = queryset.filter(
                Q(descricao__icontains=search) 
            )
        return queryset        

class listaItem(ListView):
    model = Item
    template_name = 'listaItem.html'
    context_object_name = 'itens_list'

    def get_queryset(self):
        queryset = super(listaItem, self).get_queryset()
        data = self.request.GET
        search = data.get('search')
        if search:
            queryset = queryset.filter(
                Q(descricao__icontains=search) |
                Q(categoria__descricao__icontains=search)
            )
        return queryset

def checkForFamilyId(cpf):
    chefe = Familia.objects.filter(cpfChefeFamilia__exact=cpf)
    integrante = IntegranteFamilia.objects.filter(cpf__exact=cpf)
    
    if chefe:
      return chefe.first().pk
    
    if integrante:
      return integrante.first().familia.pk

    return "DONT_EXIST"

def buscacpf(request):
    if request.method == 'POST':
        cpf = request.POST["cpf"]
        id_familia = checkForFamilyId(cpf)
        if id_familia != "DONT_EXIST":
            url = "../realizaDoacao/" + str(id_familia)
            return redirect(url)
        else:
            return render(request, 'cpfErro.html')
    return render(request, 'cpfBusca.html')

def movimentos(request, pk):
    if request.method == 'POST':
        newMovimentos = Movimentos(
            idFamilia = Familia.objects.get(pk=pk),
            representante = Representante.objects.get(nome=request.POST.get('nomeRepresentante')),
            justificativa = request.POST.get('justificativa')
        )

        newMovimentos.save()

        for item in json.loads(request.POST.get('itens')):
            newMovimentoItem = MovimentosItem(
                movimentos = Movimentos.objects.get(pk=newMovimentos.pk),
                item = Item.objects.get(descricao = item['item']),
                quantidade = item['quantity']
            )
            newMovimentoItem.save()

        url = "../../detalhesDoacao/" + str(newMovimentos.pk)
        return redirect(url)
    else:
        return render(request, 'realizaDoacao.html')

def searchFamiliaByCpf(request):
    chefeFamiliaCpf = request.GET.get('cpf')
    payload=[]

    if chefeFamiliaCpf:
        familias = Familia.objects.filter(cpfChefeFamilia__icontains=chefeFamiliaCpf)

        for familia in familias:
            payload.append(familia.cpfChefeFamilia)

    return JsonResponse({'status': 200, 'data': payload})

def searchEntidadeByName(request):
    nomeEntidade = request.GET.get('nomeEntidade')
    payload=[]

    if nomeEntidade:
        entidades = Entidade.objects.filter(nome__icontains=nomeEntidade)

        for entidade in entidades:
            payload.append(entidade.nome)

    return JsonResponse({'status': 200, 'data': payload})

def searchItemByName(request):
    nomeItem = request.GET.get('nomeItem')
    payload=[]

    if nomeItem:
        itens = Item.objects.filter(descricao__icontains=nomeItem)

        for item in itens:
            payload.append(item.descricao)

    return JsonResponse({'status': 200, 'data': payload})

def searchRepresentanteByName(request):
    nomeRepresentante = request.GET.get('nomeRepresentante')
    payload=[]

    if nomeRepresentante:
        representantes = Representante.objects.filter(nome__icontains=nomeRepresentante)

        for representante in representantes:
            payload.append(representante.nome)

    return JsonResponse({'status': 200, 'data': payload})
