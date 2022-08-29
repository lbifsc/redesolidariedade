from .models import CategoriaItem, Item
from .forms import CategoriaItemForm, ItemForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#------------------------------------------------------------------------------
# CRUD CATEGORIA 
#------------------------------------------------------------------------------

#LISTAR
class listaCategoriaItem(LoginRequiredMixin, ListView):
    model = CategoriaItem
    template_name = 'itens/listaCategoria.html'
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

#INSERIR
@login_required
def cadastroCategoriaItem(request):
    form = CategoriaItemForm()
    if request.method == 'POST':
        form = CategoriaItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista de Categorias')

    return render(request,'generic/cadastro.html',{'form': form})

#EDITAR
def editarCategoria(request, pk, template_name='generic/cadastro.html'):
    categoria = get_object_or_404(CategoriaItem, pk=pk)
    form = CategoriaItemForm(request.POST or None, instance=categoria)
    if form.is_valid():
        form.save()
        return redirect('Lista de Categorias')
    return render(request, template_name, {'form':form})

#DELETAR
def excluirCategoria(request, pk, template_name='generic/confirm_delete_cascade.html'):
    categoria = get_object_or_404(CategoriaItem, pk=pk)
    if request.method=='POST':
        categoria.delete()
        return redirect('Lista de Categorias')
    return render(request, template_name, {'object':categoria})

#------------------------------------------------------------------------------
#CRUD ITENS
#------------------------------------------------------------------------------

#LISTAR
class listaItem(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'itens/listaItem.html'
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

#INSERIR
@login_required
def cadastroItem(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista de Itens')

    return render(request,'generic/cadastro.html',{'form': form})

#EDITAR
def editarItem(request, pk, template_name='generic/cadastro.html'):
    itens = get_object_or_404(Item, pk=pk)
    form = ItemForm(request.POST or None, instance=itens)
    if form.is_valid():
        form.save()
        return redirect('Lista de Itens')
    return render(request, template_name, {'form':form})

#DELETAR
def excluirItem(request, pk, template_name='generic/confirm_delete.html'):
    item = get_object_or_404(Item, pk=pk)
    if request.method=='POST':
        item.delete()
        return redirect('Lista de Itens')
    return render(request, template_name, {'object':item})

#------------------------------------------------------------------------------
#SEARCH
#------------------------------------------------------------------------------

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