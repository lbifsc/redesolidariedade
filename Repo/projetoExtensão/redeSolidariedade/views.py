from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView

# Create your views here.

def cadastroDoacao(request):
    return render(request, 'cadastro.html')

def cadastroEntidade(request):
    if request.method == 'POST':
        form = EntidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista de Representantes')
    form = EntidadeForm()

    return render(request,'cadastro.html',{'form': form})

def cadastroFamilia(request):
    if request.method == 'POST':
        form = FamiliaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista de Familias')
    form = FamiliaForm()

    return render(request,'cadastro.html',{'form': form})

def cadastroIntegranteFamilia(request):
    if request.method == 'POST':
        form = IntegranteFamiliaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista de Familias')
    form = IntegranteFamiliaForm()

    return render(request,'cadastro.html',{'form': form})

def cadastroItem(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista de Itens')
    form = ItemForm()

    return render(request,'cadastro.html',{'form': form})

def cadastroRepresentante(request):
    if request.method == 'POST':
        form = RepresentanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista de Representantes')
    form = RepresentanteForm()

    return render(request,'cadastro.html',{'form': form})

def cadastroUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista de Usuarios')
    form = UsuarioForm()

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

def editarUsuario(request, pk, template_name='cadastro.html'):
    usuarios = get_object_or_404(Usuario, pk=pk)
    form = UsuarioForm(request.POST or None, instance=usuarios)
    if form.is_valid():
        form.save()
        return redirect('Lista de Usuarios')
    return render(request, template_name, {'form':form})

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
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method=='POST':
        usuario.delete()
        return redirect('Lista de Usuarios')
    return render(request, template_name, {'object':usuario})

class detalhesDoacao(DetailView):
    model = Movimentos
    template_name = 'detalhesDoacao.html'

class detalhesEntidade(DetailView):
    model = Entidade
    template_name ='detalhesEntidade.html'

class detalhesFamilia(DetailView):
    model = Familia
    template_name ='detalhesFamilia.html'

class detalhesRepresentante(DetailView):
    model = Representante
    template_name ='detalhesRepresentante.html'

class detalhesUsuario(DetailView):
    model = Usuario
    template_name ='detalhesUsuario.html'

def home(request):
    return render(request, 'home.html')

def relatorioDoacao(request):
    return render(request, 'relatorioDoacao.html')

def relatorioEntidade(request):
    return render(request, 'relatorioEntidade.html')

def relatorioFamilia(request):
    return render(request, 'relatorioFamilia.html')

def relatorioUsuario(request):
    return render(request, 'relatorioUsuario.html')

class listaDoacao(ListView):
   template_name = 'listaDoacao.html'
   context_object_name = 'movimentos_list'

   def get_queryset(self):
        return Movimentos.objects.all()

class listaFamilia(ListView):
    template_name = 'listaFamilia.html'
    context_object_name = 'familias_list'

    def get_queryset(self):
        return Familia.objects.all()  

class listaRepresentante(ListView):
    template_name = 'listaRepresentante.html'
    context_object_name = 'representantes_list'

    def get_queryset(self):
        return Representante.objects.all()  

class listaUsuario(ListView):
    template_name = 'listaUsuario.html'
    context_object_name = 'usuarios_list'

    def get_queryset(self):
        return Usuario.objects.all() 

class listaItem(ListView):
    template_name = 'listaItem.html'
    context_object_name = 'itens_list'

    def get_queryset(self):
        return Item.objects.all()  

def login(request):
    return render(request, 'login.html')    