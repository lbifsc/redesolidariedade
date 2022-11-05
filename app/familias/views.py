import re
from django.shortcuts import render, redirect, get_object_or_404
from .models import Familia, IntegranteFamilia
from .forms import FamiliaForm, EditFamiliaForm, IntegranteFamiliaForm
from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#------------------------------------------------------------------------------
#GENERIC
#------------------------------------------------------------------------------

def isValid(cpf) :
    if cpf == None:
        return True
    return False

#------------------------------------------------------------------------------
# CRUD FAMILIAS
#------------------------------------------------------------------------------

#LISTAR
class listaFamilia(LoginRequiredMixin, ListView):
    model = Familia
    template_name = 'familias/listaFamilia.html'
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

#DETALHAR
@login_required
def detalhesFamilia(request, pk):
    template_name = 'familias/detalhesFamilia.html'
    familia = Familia.objects.get(pk=pk)
    integrantesFamilia = IntegranteFamilia.objects.get_queryset().filter(familia=pk)
    context = {
        'familia': familia,
        'integrantesFamilia': integrantesFamilia,
    }
    return render(request, template_name, context)

#CRIAR
@login_required
def cadastroFamilia(request):
    nomePagina = 'Cadastro de Família'
    form = FamiliaForm()
    if request.method == 'POST':
        form = FamiliaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista de Familias')

    return render(request,'generic/cadastro.html',{'form': form, 'nomePagina': nomePagina})

#EDITAR
def editarFamilia(request, pk, template_name='generic/cadastro.html'):
    familias = get_object_or_404(Familia, pk=pk)
    nomePagina = 'Editar Família'
    form = EditFamiliaForm(request.POST or None, instance=familias)
    if form.is_valid():
        form.save()
        return redirect('Lista de Familias')
    return render(request, template_name, {'form':form, 'nomePagina': nomePagina})

#EXCLUIR
def excluirFamilia(request, pk, template_name='generic/confirm_delete_cascade.html'):
    familia = get_object_or_404(Familia, pk=pk)
    if request.method=='POST':
        familia.delete()
        return redirect('Lista de Familias')
    return render(request, template_name, {'object':familia})

#------------------------------------------------------------------------------
# CRUD INTEGRANTES DE FAMILIA
#------------------------------------------------------------------------------

#CADASTRAR
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
            try:
                IntegranteFamilia.objects.get(nome=novoIntegrante.nome)
                return redirect('Detalhes Familia', pk=novoIntegrante.familia.pk)
            except:
                novoIntegrante.save()
                return redirect('Detalhes Familia', pk=novoIntegrante.familia.pk)
        else:
            return redirect('Detalhes Familia', pk=cpf.familia.pk)
    return render(request,'familias/cadastroIntegranteFamiliar.html')

#EDITAR
def editarIntegranteFamilia(request, pk, template_name='generic/cadastro.html'):
    nomePagina = 'Editar Integrante de Família'
    integranteFamilia = get_object_or_404(IntegranteFamilia, pk=pk)
    form = IntegranteFamiliaForm(request.POST or None, instance=integranteFamilia)
    if form.is_valid():
        form.save()
        return redirect('Lista de Familias')
    return render(request, template_name, {'form':form, 'nomePagina': nomePagina})

#EXCLUIR
def excluirIntegranteFamilia(request, pk, template_name='generic/confirm_delete.html'):
    integranteFamilia = get_object_or_404(IntegranteFamilia, pk=pk)
    if request.method=='POST':
        integranteFamilia.delete()
        return redirect('Lista de Familias')
    return render(request, template_name, {'object':integranteFamilia})

#------------------------------------------------------------------------------
