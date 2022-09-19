import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import Group
from django.db.models import Q
from .models import Entidade, Representante
from django.contrib import messages
from .forms import EntidadeForm, RepresentanteForm, RedefinirSenhaForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Permission

#------------------------------------------------------------------------------
#GENERIC
#------------------------------------------------------------------------------

def isValid(cpf) :
    if cpf == None:
        return True
    return False

#------------------------------------------------------------------------------
# CRUD ENTIDADES DE REPRESENTANTE
#------------------------------------------------------------------------------

#LISTAR
class listaEntidades(LoginRequiredMixin, ListView):
    model = Entidade
    template_name = 'grupos/listaEntidades.html'
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

#DETALHAR
class detalhesEntidade(LoginRequiredMixin, DetailView):
    model = Entidade
    template_name ='grupos/detalhesEntidade.html'

#CRIAR
@login_required
def cadastroEntidade(request):
    nomePagina = 'Cadastro de Entidade'
    form = EntidadeForm()
    if request.method == 'POST':
        form = EntidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista de Entidades')

    return render(request,'generic/cadastro.html',{'form': form, 'nomePagina': nomePagina})

#EDITAR
def editarEntidade(request, pk, template_name='generic/cadastro.html'):
    nomePagina = 'Editar Entidade'
    entidades = get_object_or_404(Entidade, pk=pk)
    form = EntidadeForm(request.POST or None, instance=entidades)
    if form.is_valid():
        form.save()
        return redirect('Lista de Entidades')
    return render(request, template_name, {'form':form, 'nomePagina': nomePagina})

#EXCLUIR
def excluirEntidade(request, pk, template_name='generic/confirm_delete_cascade.html'):
    entidade = get_object_or_404(Entidade, pk=pk)
    if request.method=='POST':
        entidade.delete()
        return redirect('Lista de Entidades')
    return render(request, template_name, {'object':entidade})

#------------------------------------------------------------------------------
# CRUD REPRESENTANTES
#------------------------------------------------------------------------------

#LISTAR
class listaRepresentante(LoginRequiredMixin, ListView):
    model = Representante
    template_name = 'grupos/listaRepresentante.html'
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

#DETALHAR
class detalhesRepresentante(LoginRequiredMixin, DetailView):
    model = Representante
    template_name ='grupos/detalhesRepresentante.html'

#CADASTRAR
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
                password='novousuario'
                )

                relatedUser.save()
                grupo, foiCriado = Group.objects.get_or_create(name='primeirologin')
                relatedUser.groups.add(grupo)

                return redirect('Lista de Representantes')
        else:
           return redirect('Detalhes Representante', pk=cpf.pk)

    return render(request,'grupos/cadastroRepresentante.html')

#EDITAR
def editarRepresentante(request, pk, template_name='generic/cadastro.html'):
    nomePagina = 'Editar Representante'
    representantes = get_object_or_404(Representante, pk=pk)
    form = RepresentanteForm(request.POST or None, instance=representantes)
    if form.is_valid():
        form.save()
        return redirect('Lista de Representantes')
    return render(request, template_name, {'form':form, 'nomePagina': nomePagina})

#EXCLUIR
def excluirRepresentante(request, pk, template_name='generic/confirm_delete.html'):
    representante = get_object_or_404(Representante, pk=pk)
    usuario = User.objects.get(username=representante.nome)
    if request.method=='POST':
        representante.delete()
        usuario.is_active = False
        return redirect('Lista de Representantes')
    return render(request, template_name, {'object':representante})

#------------------------------------------------------------------------------
# CRUD USUARIOS USUARIOS
#------------------------------------------------------------------------------

#LISTAR
class listaUsuario(LoginRequiredMixin, ListView):
    model = User
    template_name = 'grupos/listaUsuario.html'
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

#INATIVAR
def inativarUsuario(request, pk):
    erro = ''
    usuario = get_object_or_404(User, pk=pk)
    try:
        if request.method=='POST':
            
            # Verificando se usuário é administrador
            if request.user.is_superuser is False:
                erro = "Você não tem permissão para inativar usuários. Solicite a um usuário administrador."
                raise Exception(erro)
            
            # Impedir usuário de inativar o próprio cadastro e perder acesso ao sistema
            if request.user == usuario:
                erro = "Você não pode inativar seu próprio usuário. Solicite a outro usuário administrador."
                raise Exception(erro)

            usuario.is_active = False
            usuario.save()
            messages.success(request, "Usuário inativado com sucesso.", extra_tags='alert alert-success px-2')
            return redirect('Editar Usuário', pk=usuario.pk)
        else:
            return render(request,'registration/editarUsuario.html',{'usuarioAlterado': usuario, 'object': usuario})
        
    except Exception as excecao:
        erro = "Tente novamente: " + str(excecao)
        messages.warning(request, erro, extra_tags='alert alert-danger px-2')
        return redirect('Editar Usuário', pk = usuario.pk)



#REATIVAR
def reativarUsuario(request, pk):
    erro = ''
    usuario = get_object_or_404(User, pk=pk)
    try:
        if request.method=='POST':
            
            # Verificando se usuário é administrador
            if request.user.is_superuser is False:
                erro = "Você não tem permissão para reativar usuários. Solicite a um usuário administrador."
                raise Exception(erro)
            
            usuario.is_active = True
            usuario.save()
            messages.success(request, "Usuário reativado com sucesso.", extra_tags='alert alert-success px-2')
            return redirect('Editar Usuário', pk=usuario.pk)
        else:
            return render(request,'registration/editarUsuario.html',{'usuarioAlterado': usuario, 'object': usuario})
        
    except Exception as excecao:
        erro = "Tente novamente: " + str(excecao)
        messages.warning(request, erro, extra_tags='alert alert-danger px-2')
        return redirect('Editar Usuário', pk = usuario.pk)

#EDITAR
@login_required
def editarUsuario(request, pk, template_name='generic/cadastro.html'):
    erro = ''
    usuarioAlterado = get_object_or_404(User, pk=pk)

    #Formatando data de cadastro e último login apenas para exibição na tela
    usuarioAlterado.date_joined = usuarioAlterado.date_joined.strftime("%d/%m/%Y   %H:%M:%S")
    try:
        # Verificando se usuário já logou alguma vez pra não tentar formatar uma data com valor nulo
        usuarioAlterado.last_login = usuarioAlterado.last_login.strftime("%d/%m/%Y   %H:%M:%S")
    except:
        usuarioAlterado.last_login = "Usuário ainda não logou"

    try:
        if request.method == 'POST':
            usuario = get_object_or_404(User, pk=pk)

            # Verificando se usuário é administrador
            if request.user.is_superuser is False:
                erro = "Você não tem permissão para alterar usuários. Solicite a um usuário administrador."
                raise Exception(erro)

            usuario.first_name = request.POST.get('primeiroNome')
            usuario.last_name = request.POST.get('sobrenome')
            usuario.email = request.POST.get('email')

            if request.POST.get('usuarioAdministrador', "") == "on": # Se checkbox foi marcado
                usuario.is_superuser = True
                usuario.is_staff = True
            elif request.POST.get('usuarioAdministrador', "") != "on": # Se checkbox não foi marcado
                usuario.is_superuser = False
                usuario.is_staff = False

            usuario.save()
            messages.success(request, "Dados atualizados com sucesso.", extra_tags='alert alert-success px-2')

            return redirect('Editar Usuário', pk=usuario.pk)

        else: # se for GET
            return render(request,'registration/editarUsuario.html',{'usuarioAlterado': usuarioAlterado, 'object':usuarioAlterado})

    except Exception as excecao:
        erro = "Tente novamente: " + str(excecao)
        messages.warning(request, erro, extra_tags='alert alert-danger px-2')
        return render(request,'registration/editarUsuario.html', {'usuarioAlterado': usuarioAlterado, 'object':usuarioAlterado})


#VIEW REDEFINIR SENHA
@login_required
def redefinirSenha(request):
    erro = ''
    user = request.user
    ehPaginaRedefinicaoSenha = True
    try:
        if request.method == 'POST':
            novaSenha = request.POST.get('novaSenhaConfirmacao')
            senhaAtualDigitada = request.POST.get('senhaAtual')
            senhaAtual = user.password

            # Verifica se senha atual coincide com a cadastrada
            if check_password(senhaAtualDigitada, senhaAtual) == False:
                erro = 'A senha atual não coincide com a cadastrada para este usuário.'
                raise Exception(erro)

            # Tratamento de erros dos requisitos da senha
            # Se contém espaço em branco ou é uma string vazia
            if novaSenha.find(" ") != -1 or novaSenha == '':
                erro = 'A senha não pode conter espaço em branco. Utilize apenas letras, números e/ou caracteres especiais.'
                raise Exception(erro)

            # Se for menor que 4 caracteres
            if len(novaSenha) < 4:
                erro = 'Sua nova senha precisa ter no mínimo 4 caracteres.'
                raise Exception(erro)

            # Verifica se as duas senhas digitadas coincidem
            if request.POST.get('novaSenha') != request.POST.get('novaSenhaConfirmacao'):
                erro = 'As senhas digitadas não coincidem. Certifique-se de que as novas senhas digitadas são iguais.'
                raise Exception(erro)

            # Verifica se a nova senha é igual a senha atual
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
            return render(request,'registration/redefinirSenha.html',{'form': form, "ehPaginaRedefinicaoSenha": ehPaginaRedefinicaoSenha})

    except Exception as excecao:
        if excecao is not None: #Se cair em um erro não tratado acima, retorna a mensagem do Django
            erro = "Tente novamente: " + str(excecao)
            messages.warning(request, erro, extra_tags='alert alert-danger px-2')
        else:
            messages.warning(request, erro, extra_tags='alert alert-danger px-2')
        form = RedefinirSenhaForm()
        return render(request,'registration/redefinirSenha.html', {'form': form, "ehPaginaRedefinicaoSenha": ehPaginaRedefinicaoSenha})

#VIEW REDEFINIR SENHA COMPLETA
def redefinicaoSenhaCompleta(request):
    return render(request, 'registration/redefinicaoSenhaCompleta.html')

#VIEW PRIMEIRO LOGIN (solicita alteração de senha)
def primeiroLogin(request):
    return render(request, 'registration/primeiroLogin.html')


#------------------------------------------------------------------------------
