from django.shortcuts import render
from django.contrib import messages

from .forms import CodelistsPanModelForm, UsuariosPanModelForm
from .models import CodelistsPanProd


def index_pp(request):
    return render(request, 'panpharma_producao/index_pp.html')


def cad_codelist(request):
    if str(request.method) == 'POST':
        form = CodelistsPanModelForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Dados enviados com sucesso!')
            form.save()
            form = CodelistsPanModelForm
        else:
            messages.error(request, 'Erro ao enviar o formulário!')
    else:
        form = CodelistsPanModelForm

    context = {
        'form': form
    }

    return render(request, 'panpharma_producao/cad_codelist.html', context)


def cons_codelists(request):
    objects = CodelistsPanProd.objects.all()
    context = {
        'codelists': objects
    }
    return render(request, 'panpharma_producao/cons_codelists.html', context)


def cad_usuarios(request):
    if str(request.method) == 'POST':
        form = UsuariosPanModelForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Dados enviados com sucesso!')
            form.save()
            form = UsuariosPanModelForm
        else:
            messages.error(request, 'Erro ao enviar o formulário!')
    else:
        form = UsuariosPanModelForm

    context = {
        'form': form
    }

    return render(request, 'panpharma_producao/cad_usuarios.html', context)


def exc_codelist(request):
    return render(request, 'panpharma_producao/exc_codelist.html')


def exc_usuarios(request):
    return render(request, 'panpharma_producao/exc_usuarios.html')