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
import re
from django.core.paginator import Paginator
from django.contrib.auth.password_validation import *
from django.contrib import messages
from dateutil.parser import parse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import check_password

# Create your views here.

def cadastroDoacao(request):
    return render(request, 'cadastro.html')

@login_required
def cadastroEntidade(request):
    form = EntidadeForm()
    if request.method == 'POST':
        form = EntidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista de Entidades')

    return render(request,'cadastro.html',{'form': form})

@login_required
def cadastroFamilia(request):
    form = FamiliaForm()
    if request.method == 'POST':
        form = FamiliaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista de Familias')

    return render(request,'cadastro.html',{'form': form})

def isValid(cpf) :
    if cpf == None:
        return True
    return False

@login_required
def cadastroIntegranteFamilia(request):
    if request.method == 'POST':
        try:
            cpf = IntegranteFamilia.objects.get(cpf=str(re.sub('[^0-9]', '', request.POST.get('cpfIntegrante'))))
        except:
            cpf = None

        if isValid(cpf):
            nomeChefeFamilia = request.POST.get('idFamilia')
            nomeChefeFamilia = nomeChefeFamilia.split(' -- CPF:')
            novoIntegrante = IntegranteFamilia(
                familia = Familia.objects.get(nomeChefeFamilia=nomeChefeFamilia[0]),
                nome = request.POST.get('nomeIntegrante'),
                cpf = re.sub('[^0-9]', '', request.POST.get('cpfIntegrante'))
            )
            novoIntegrante.save()
            return redirect('Lista de Familias')
        else:
            return redirect('Detalhes Familia', pk=cpf.familia.pk)
    return render(request,'cadastroIntegranteFamiliar.html')

@login_required
def cadastroCategoriaItem(request):
    form = CategoriaItemForm()
    if request.method == 'POST':
        form = CategoriaItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista de Categorias')

    return render(request,'cadastro.html',{'form': form})

@login_required
def cadastroItem(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista de Itens')

    return render(request,'cadastro.html',{'form': form})

@login_required
def cadastroRepresentante(request):
    if request.method == 'POST':
        try:
            cpf = Representante.objects.get(cpf=str(re.sub('[^0-9]', '', request.POST.get('cpfRepresentante'))))
        except:
            cpf = None

        if isValid(cpf):

            if Representante.objects.filter(nome=(request.POST.get('nomeRepresentante'))).exists():
                rep = Representante.objects.get(nome=(request.POST.get('nomeRepresentante')))
                return redirect('Detalhes Representante', pk=rep.pk)
            else:
                novoRepresentante = Representante(idEntidade = Entidade.objects.get(nome=request.POST.get('nomeEntidade')),
                    nome = request.POST.get('nomeRepresentante'),
                    cpf = re.sub('[^0-9]', '', request.POST.get('cpfRepresentante')),
                    endereco = request.POST.get('endereco'),
                    observacao = request.POST.get('observacao')
                )

                novoRepresentante.save()

                relatedUser = User.objects.create_user(
                username= novoRepresentante.nome,
                email= novoRepresentante.nome,
                password='NOVOUSUARIO'
                )

                relatedUser.save()
                grupo, foiCriado = Group.objects.get_or_create(name='primeirologin')
                relatedUser.groups.add(grupo)
                relatedUser.groups.add(Group.objects.get(name='user_common'))

                return redirect('Lista de Representantes')
        else:
           return redirect('Detalhes Representante', pk=cpf.pk)

    return render(request,'cadastroRepresentante.html')

@login_required
def redefinirSenha(request):
    erro = ''
    user = request.user
    try:
        if request.method == 'POST':
            novaSenha = request.POST.get('novaSenhaConfirmacao')

            # Tratamento de erros dos requisitos da senha
            #Se contém espaço em branco ou é uma string vazia
            if novaSenha.find(" ") != -1 or novaSenha == '':
                erro = 'A senha não pode conter espaço em branco. Utilize apenas letras, números e/ou caracteres especiais.'
                raise Exception(erro)

            #Se for menor que 4 caracteres
            if len(novaSenha) < 4:
                erro = 'Sua nova senha precisa ter no mínimo 4 caracteres.'
                raise Exception(erro)

            # Verifica se as duas senhas digitadas coincidem, se não, lança uma exceção e retorna o erro para o usuário
            if request.POST.get('novaSenha') != request.POST.get('novaSenhaConfirmacao'):
                erro = 'As senhas digitadas não coincidem. Certifique-se de que as senhas são iguais.'
                raise Exception(erro)

            # Verifica se a nova senha é igual a senha atual
            senhaAtual = user.password
            if check_password(novaSenha, senhaAtual):
                erro = 'Sua nova senha não pode ser igual a senha atual.'
                raise Exception(erro)

            user = request.user
            user.set_password(novaSenha)
            # Após a primeira alteração de senha, retira o usuário do grupo "primeiroLogin" e não solicita redefinição no primeiro login
            if user.groups.filter(name = 'primeirologin').exists():
                grupoAremover = Group.objects.get(name='primeirologin')
                user.groups.remove(grupoAremover)
            user.save()
            return redirect('Redefinição de Senha Completa')

        else:
            form = RedefinirSenhaForm()
            return render(request,'registration/redefinirSenha.html',{'form': form})

    except Exception as excecao:
        if excecao is not None: #Se cair em um erro não tratado acima, retorna a mensagem do Django
            erro = "Tente novamente: " + str(excecao)
            messages.warning(request, erro, extra_tags='alert alert-danger px-2')
        else:
            messages.warning(request, erro, extra_tags='alert alert-danger px-2')
        form = RedefinirSenhaForm()
        return render(request,'registration/redefinirSenha.html', {'form': form})

def redefinicaoSenhaCompleta(request):
    return render(request, 'registration/redefinicaoSenhaCompleta.html')

def editarDoacao(request):
    return render(request, 'cadastro.html')

def editarEntidade(request, pk, template_name='cadastro.html'):
    entidades = get_object_or_404(Entidade, pk=pk)
    form = EntidadeForm(request.POST or None, instance=entidades)
    if form.is_valid():
        form.save()
        return redirect('Lista de Entidades')
    return render(request, template_name, {'form':form})

def editarFamilia(request, pk, template_name='cadastro.html'):
    familias = get_object_or_404(Familia, pk=pk)
    form = EditFamiliaForm(request.POST or None, instance=familias)
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
    form = EditRepresentanteForm(request.POST or None, instance=representantes)
    if form.is_valid():
        form.save()
        return redirect('Lista de Representantes')
    return render(request, template_name, {'form':form})

def excluirCategoria(request, pk, template_name='confirm_delete_cascade.html'):
    categoria = get_object_or_404(CategoriaItem, pk=pk)
    if request.method=='POST':
        categoria.delete()
        return redirect('Lista de Categorias')
    return render(request, template_name, {'object':categoria})

def excluirDoacao(request, pk, template_name='confirm_delete_cascade.html'):
    doacao = get_object_or_404(Movimentos, pk=pk)
    if request.method=='POST':
        doacao.delete()
        return redirect('Lista de Doações')
    return render(request, template_name, {'object':doacao})

def excluirEntidade(request, pk, template_name='confirm_delete_cascade.html'):
    entidade = get_object_or_404(Entidade, pk=pk)
    if request.method=='POST':
        entidade.delete()
        return redirect('Lista de Entidades')
    return render(request, template_name, {'object':entidade})

def excluirFamilia(request, pk, template_name='confirm_delete_cascade.html'):
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

@login_required
def detalhesDoacao(request, pk):
    template_name = 'detalhesDoacao.html'
    movimento = Movimentos.objects.get(pk=pk)
    movimentosItens = MovimentosItem.objects.get_queryset().filter(movimentos=pk)
    context = {
        'movimento': movimento,
        'movimentosItens': movimentosItens,
    }
    return render(request, template_name, context)

class detalhesEntidade(LoginRequiredMixin, DetailView):
    model = Entidade
    template_name ='detalhesEntidade.html'

@login_required
def detalhesFamilia(request, pk):
    template_name = 'detalhesFamilia.html'
    familia = Familia.objects.get(pk=pk)
    integrantesFamilia = IntegranteFamilia.objects.get_queryset().filter(familia=pk)
    context = {
        'familia': familia,
        'integrantesFamilia': integrantesFamilia,
    }
    return render(request, template_name, context)

class detalhesRepresentante(LoginRequiredMixin, DetailView):
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

@login_required
def relatorioDoacao(request):
    return render(request, 'relatorioDoacao.html')

@login_required
def relatorioEntidade(request):
    return render(request, 'relatorioEntidade.html')

@login_required
def relatorioFamilia(request):
    return render(request, 'relatorioFamilia.html')

@login_required
def relatorioUsuario(request):
    return render(request, 'relatorioUsuario.html')

class listaDoacao(LoginRequiredMixin, ListView):
    model = Movimentos
    template_name = 'listaDoacao.html'
    context_object_name = 'movimentos_list'
    paginate_by = 8

    def get_queryset(self):

        queryset = super(listaDoacao, self).get_queryset()
        data = self.request.GET
        search = data.get('search')

        data_inicial = self.request.GET.get('data_inicial')
        data_final = self.request.GET.get('data_final')

        if search:
            if data_inicial and data_final:
                queryset = queryset.filter(
                    Q(idFamilia__nomeChefeFamilia__icontains=search)|
                    Q(data__range=[data_inicial, data_final])
                )
            else:
                queryset = queryset.filter(
                    Q(idFamilia__nomeChefeFamilia__icontains=search)
                )

        if data_inicial and data_final:
            data_final = parse(data_final) + timedelta(1)
            queryset = queryset.filter(
                data__range=[data_inicial, data_final]
            )

        return queryset

class listaFamilia(LoginRequiredMixin, ListView):
    model = Familia
    template_name = 'listaFamilia.html'
    context_object_name = 'familias_list'
    paginate_by = 8

    def get_queryset(self):
        queryset = super(listaFamilia, self).get_queryset()
        data = self.request.GET
        search = data.get('search')
        if search:
            queryset = queryset.filter(
                Q(nomeChefeFamilia__icontains=search) |
                Q(cpfChefeFamilia__icontains=search)
            )
        return queryset

class listaRepresentante(LoginRequiredMixin, ListView):
    model = Representante
    template_name = 'listaRepresentante.html'
    context_object_name = 'representantes_list'
    paginate_by = 8

    def get_queryset(self):
        queryset = super(listaRepresentante, self).get_queryset()
        data = self.request.GET
        search = data.get('search')
        if search:
            queryset = queryset.filter(
                Q(nome__icontains=search) |
                Q(cpf__icontains=search)
            )
        return queryset

class listaUsuario(LoginRequiredMixin, ListView):
    model = User
    template_name = 'listaUsuario.html'
    context_object_name = 'usuarios_list'
    paginate_by = 8

    def get_queryset(self):
        queryset = super(listaUsuario, self).get_queryset()
        data = self.request.GET
        search = data.get('search')
        if search:
            queryset = queryset.filter(
                Q(username__icontains=search)
            )
        return queryset

class listaEntidades(LoginRequiredMixin, ListView):
    model = Entidade
    template_name = 'listaEntidades.html'
    context_object_name = 'entidades_list'
    paginate_by = 8

    def get_queryset(self):
        queryset = super(listaEntidades, self).get_queryset()
        data = self.request.GET
        search = data.get('search')
        if search:
            queryset = queryset.filter(
                Q(nome__icontains=search)
            )
        return queryset

class listaCategoriaItem(LoginRequiredMixin, ListView):
    model = CategoriaItem
    template_name = 'listaCategoria.html'
    context_object_name = 'categoriaItens_list'
    paginate_by = 8

    def get_queryset(self):
        queryset = super(listaCategoriaItem, self).get_queryset()
        data = self.request.GET
        search = data.get('search')
        if search:
            queryset = queryset.filter(
                Q(descricao__icontains=search)
            )
        return queryset

class listaItem(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'listaItem.html'
    context_object_name = 'itens_list'
    paginate_by = 2

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


@login_required()
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

@login_required()
def movimentos(request, pk):
    if request.method == 'POST':
        newMovimentos = Movimentos(
            idFamilia = Familia.objects.get(pk=pk),
            representante = Representante.objects.get(nome=request.user),
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
        user = request.user
        doacoesAnteriores = Movimentos.objects.filter(idFamilia__exact=pk).order_by('-data')[:5]
        return render(request, 'realizaDoacao.html',{'user': user, 'doacoesAnteriores': doacoesAnteriores})

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

def searchCategoriaByName(request):
    nomeCategoria = request.GET.get('nomeCategoria')
    payload=[]

    if nomeCategoria:
        categorias = CategoriaItem.objects.filter(descricao__icontains=nomeCategoria)

        for categoria in categorias:
            payload.append(categoria.descricao)

    return JsonResponse({'status': 200, 'data': payload})

def searchRepresentanteByName(request):
    nomeRepresentante = request.GET.get('nomeRepresentante')
    payload=[]

    if nomeRepresentante:
        representantes = Representante.objects.filter(nome__icontains=nomeRepresentante)

        for representante in representantes:
            payload.append(representante.nome)

    return JsonResponse({'status': 200, 'data': payload})

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