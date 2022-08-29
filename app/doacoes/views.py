import json
from .models import Movimentos, MovimentosItem
from familias.models import Familia, IntegranteFamilia
from grupos.models import Representante
from itens.models import Item
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from datetime import timedelta
from django.db.models import Q
from dateutil.parser import parse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#------------------------------------------------------------------------------
#GENERIC
#------------------------------------------------------------------------------

def checkForFamilyId(cpf):
    chefe = Familia.objects.filter(cpfChefeFamilia__exact=cpf)
    integrante = IntegranteFamilia.objects.filter(cpf__exact=cpf)

    if chefe:
      return chefe.first().pk

    if integrante:
      return integrante.first().familia.pk

    return "DONT_EXIST"

#------------------------------------------------------------------------------
# CRUD FAMILIAS
#------------------------------------------------------------------------------

#LISTAR
class listaDoacao(LoginRequiredMixin, ListView):
    model = Movimentos
    template_name = 'doacoes/listaDoacao.html'
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

#DETALHAR
@login_required
def detalhesDoacao(request, pk):
    template_name = 'doacoes/detalhesDoacao.html'
    movimento = Movimentos.objects.get(pk=pk)
    movimentosItens = MovimentosItem.objects.get_queryset().filter(movimentos=pk)
    context = {
        'movimento': movimento,
        'movimentosItens': movimentosItens,
    }
    return render(request, template_name, context)

#CRIAR
@login_required()
def buscacpf(request):
    if request.method == 'POST':
        cpf = request.POST["cpf"]
        id_familia = checkForFamilyId(cpf)
        if id_familia != "DONT_EXIST":
            url = "../realizaDoacao/" + str(id_familia)
            return redirect(url)
        else:
            return render(request, 'doacoes/cpfErro.html')
    return render(request, 'doacoes/cpfBusca.html')

#REALIZAR DOACAO
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
        return render(request, 'doacoes/realizaDoacao.html',{'user': user, 'doacoesAnteriores': doacoesAnteriores})

#EXCLUIR
def excluirDoacao(request, pk, template_name='generic/confirm_delete_cascade.html'):
    doacao = get_object_or_404(Movimentos, pk=pk)
    if request.method=='POST':
        doacao.delete()
        return redirect('Lista de Doações')
    return render(request, template_name, {'object':doacao})

#------------------------------------------------------------------------------