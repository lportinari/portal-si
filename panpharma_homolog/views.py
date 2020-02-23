from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView

from .forms import TesteModelForm, UsuariosPanModelForm, CodelistsPanModelForm, SearchCodelists
from .models import UsuariosPanHomol, CodelistsPanHomol


def index_ph(request):
    return render(request, 'panpharma_homolog/index_ph.html')


def cad_codelist(request):
    if str(request.method) == 'POST':
        form = CodelistsPanModelForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Dados enviados com sucesso!')
            form.save()
            form = CodelistsPanModelForm()
        else:
            messages.error(request, 'Erro ao enviar o formulário!')
    else:
        form = CodelistsPanModelForm()

    context = {
        'form': form
    }

    return render(request, 'panpharma_homolog/cad_codelist.html', context)


def cons_codelists(request):
    objects = CodelistsPanHomol.objects.all()
    context = {
        'codelists': objects
    }
    return render(request, 'panpharma_homolog/cons_codelists.html', context)


def cad_usuarios(request):
    if str(request.method) == 'POST':
        form = UsuariosPanModelForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Dados enviados com sucesso!')
            form.save()
            form = UsuariosPanModelForm()
        else:
            messages.error(request, 'Erro ao enviar o formulário!')
    else:
        form = UsuariosPanModelForm()

    context = {
        'form': form
    }
    return render(request, 'panpharma_homolog/cad_usuarios.html', context)


def exc_codelist(request):
    return render(request, 'panpharma_homolog/exc_codelist.html')


def exc_usuarios(request):
    return render(request, 'panpharma_homolog/exc_usuarios.html')


def teste(request):
    objects = CodelistsPanHomol.objects.all()

    context = {
        'codelists': objects
    }
    return render(request, 'panpharma_homolog/teste.html', context)

'''
class BuscarCodelist(TemplateView):

    def search(self, request, *args, **kwargs):
        busca = request.post('search_codelists')
        print(busca)
        return render(request, 'panpharma_producao/cons_codelists.html')
'''


