from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormConfiabilidadeEmpresa
from home.models import ConfiabilidadeEmpresa
import os
import json
from processamento.src.processar_financas import enviar_notas_fiscais, \
    enviar_debitos

# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method != 'POST':
        return render(request, 'login/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos')
        return render(request, 'login/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login efetuado')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado')
    return redirect('home')


def cadastro(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method != 'POST':
        return render(request, 'login/cadastro.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not usuario or not senha or not senha2:
        messages.error(request, 'Todos os campos devem ser preenchidos')
        return render(request, 'login/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existente')
        return render(request, 'login/cadastro.html')

    if senha != senha2:
        messages.error(request, 'Senhas distintas')
        return render(request, 'login/cadastro.html')

    user = User.objects.create_user(username=usuario, password=senha)
    user.save()
    messages.success(request, 'Usário cadastrado')
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'login/dashboard.html')


@login_required(redirect_field_name='login')
def addempresa(request):
    parametros = ConfiabilidadeEmpresa.objects.all()
    if request.method != 'POST':
        form = FormConfiabilidadeEmpresa()
        return render(request, 'login/addempresa.html', {
            'form': form,
            'parametros': parametros,
        })

    form = FormConfiabilidadeEmpresa(request.POST, request.FILES)
    if not form.is_valid:
        messages.error(request, 'Erro ao adicionar empresa')
        form = FormConfiabilidadeEmpresa(request.POST)
        return render(request, 'login/addempresa.html', {
            'form': form,
            'parametros': parametros,
        })

    form.save()
    messages.success(request, 'Empresa adicionada')
    return redirect('dashboard')


@login_required(redirect_field_name='login')
def enviarfinancas(request):
    parametros = ConfiabilidadeEmpresa.objects.all()
    if request.method != 'POST':
        return render(request, 'login/enviarfinancas.html', {
            'parametros': parametros,
        })

    empresa = request.POST.get('empresaselecionada')
    arquivo = request.FILES.get('arquivo')

    if not arquivo:
        messages.error(request, 'Selecione um arquivo para enviar')
        return render(request, 'login/enviarfinancas.html', {
            'parametros': parametros,
        })

    ext_arquivo = os.path.splitext(str(arquivo))[1]

    if ext_arquivo != '.json':
        messages.error(request, 'Selecione um arquivo json')
        return render(request, 'login/enviarfinancas.html', {
            'parametros': parametros,
        })

    with open('processamento/financas.json', 'wb+') as destination:
        for chunk in arquivo.chunks():
            destination.write(chunk)

    with open('processamento/financas.json', 'r') as arquivo:
        data = json.load(arquivo)

    try:
        data['nf']
    except KeyError:
        messages.error(
            request, 'Arquivo não possui a quantidade de notas fiscais')
        return render(request, 'login/enviarfinancas.html', {
            'parametros': parametros,
        })

    if type(data['nf']) != int or data['nf'] < 0:
        messages.error(
            request, 'Quantidade de notas fiscais deve ser número inteiro positivo ou nulo')
        return render(request, 'login/enviarfinancas.html', {
            'parametros': parametros,
        })

    try:
        data['d']
    except KeyError:
        messages.error(request, 'Arquivo não possui a quantidade de débitos')
        return render(request, 'login/enviarfinancas.html', {
            'parametros': parametros,
        })

    if type(data['d']) != int or data['d'] < 0:
        messages.error(
            request, 'Quantidade de débitos deve ser número inteiro positivo ou nulo')
        return render(request, 'login/enviarfinancas.html', {
            'parametros': parametros,
        })

    indice_antigo = ConfiabilidadeEmpresa.objects.filter(id=empresa)[0].indice
    indice_atualizado = enviar_notas_fiscais(data['nf'], indice_antigo)
    indice_atualizado = enviar_debitos(data['d'], indice_atualizado)
    ConfiabilidadeEmpresa.objects.filter(
        id=empresa).update(indice=indice_atualizado)

    messages.success(request, 'Envio efetuado')
    return redirect('dashboard')
