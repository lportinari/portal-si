from django.contrib import admin

from .models import UsuariosSantaHomol, CodelistsSantaHomol

# Registrando a tabela na página administrativa
@admin.register(UsuariosSantaHomol)
class UsuariosSantaHomolAdmin(admin.ModelAdmin):
    list_display = (
        'codigo_cliente', 'mapa', 'van', 'apontador', 'quebra', 'mapa_retorno_atendidos', 'mapa_retorno_nao_atendidos',
        'extensao_retorno_itens_atendidos', 'extensao_retorno_itens_nao_atendidos', 'mascara_retorno_atendidos',
        'mascara_retorno_nao_atendidos', 'sobrepoe_arquivo', 'mapa_retorno_nf', 'mascara_nf', 'extensao_nf',
        'sobrepoe_nf', 'usuario_arquivo_preco', 'mascara_remessa_arq_preco', 'move_arq_preco', 'diretorio_arq_preco'
    )


@admin.register(CodelistsSantaHomol)
class CodelistsSantaHomolAdmin(admin.ModelAdmin):
    list_display = (
        'codigo_cliente', 'mapa', 'van', 'apontador', 'quebra', 'mapa_retorno_atendidos', 'mapa_retorno_nao_atendidos',
        'extensao_retorno_itens_atendidos', 'extensao_retorno_itens_nao_atendidos', 'mascara_retorno_atendidos',
        'mascara_retorno_nao_atendidos', 'sobrepoe_arquivo', 'mapa_retorno_nf', 'mascara_nf', 'extensao_nf',
        'sobrepoe_nf', 'usuario_arquivo_preco', 'mascara_remessa_arq_preco', 'move_arq_preco', 'diretorio_arq_preco'
    )
