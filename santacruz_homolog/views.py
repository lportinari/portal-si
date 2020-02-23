from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from .forms import UsuariosSantaModelForm, CodelistsSantaModelForm
from .models import CodelistsSantaHomol


def index(request):
    return render(request, 'index.html')


def index_sh(request):
    return render(request, 'santacruz_homolog/index_sh.html')


def cad_codelist(request):
    if str(request.method) == 'POST':
        form = CodelistsSantaModelForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Dados enviados com sucesso!')
            form.save()
            form = CodelistsSantaModelForm
        else:
            messages.error(request, 'Erro ao enviar o formulário!')
    else:
        form = CodelistsSantaModelForm

    context = {
        'form': form
    }

    return render(request, 'santacruz_homolog/cad_codelist.html', context)


def cons_codelists(request):
    objects = CodelistsSantaHomol.objects.all()
    context = {
        'codelists': objects
    }
    return render(request, 'santacruz_homolog/cons_codelists.html', context)


def cad_usuarios(request):
    if str(request.method) == 'POST':
        form = UsuariosSantaModelForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Dados enviados com sucesso!')
            form.save()
            form = UsuariosSantaModelForm
        else:
            messages.error(request, 'Erro ao enviar o formulário!')
    else:
        form = UsuariosSantaModelForm

    context = {
        'form': form
    }
    return render(request, 'santacruz_homolog/cad_usuarios.html', context)


def exc_codelist(request):
    return render(request, 'santacruz_homolog/exc_codelist.html')


def exc_usuarios(request):
    return render(request, 'santacruz_homolog/exc_usuarios.html')
