from django.urls import path

from . import views

app_name = 'panpharma_producao'

urlpatterns = [
    path('index_pp', views.index_pp, name='index_pp'),
    path('cad_codelist', views.cad_codelist, name='cad_codelist'),
    path('cons_codelists', views.cons_codelists, name='cons_codelists'),
    path('cad_usuarios', views.cad_usuarios, name='cad_usuarios'),
    path('exc_codelist', views.exc_codelist, name='exc_codelist'),
    path('exc_usuarios', views.exc_usuarios, name='exc_usuarios'),
]
