from django.shortcuts import render
from .models import ConfiabilidadeEmpresa

# Create your views here.


def index(request):
    parametros = ConfiabilidadeEmpresa.objects.order_by('-indice')
    return render(request, 'home/index.html', {
        'parametros': parametros
    })


def ver_empresa(request, confiabilidadeempresa_id):
    parametro = ConfiabilidadeEmpresa.objects.get(id=confiabilidadeempresa_id)
    return render(request, 'home/ver_empresa.html', {
        'parametro': parametro
    })


def sobre(request):
    return render(request, 'home/sobre.html')
