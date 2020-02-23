from django import forms

from .models import UsuariosSantaHomol, CodelistsSantaHomol


class UsuariosSantaModelForm(forms.ModelForm):
    class Meta:
        model = UsuariosSantaHomol
        fields = ['codigo_cliente', 'mapa', 'van', 'apontador', 'quebra', 'mapa_retorno_atendidos',
                  'mapa_retorno_nao_atendidos', 'extensao_retorno_itens_atendidos',
                  'extensao_retorno_itens_nao_atendidos', 'mascara_retorno_atendidos', 'mascara_retorno_nao_atendidos',
                  'sobrepoe_arquivo', 'mapa_retorno_nf', 'mascara_nf', 'extensao_nf', 'sobrepoe_nf',
                  'usuario_arquivo_preco', 'mascara_remessa_arq_preco', 'move_arq_preco', 'diretorio_arq_preco']


class CodelistsSantaModelForm(forms.ModelForm):
    class Meta:
        model = CodelistsSantaHomol
        fields = ['codigo_cliente', 'mapa', 'van', 'apontador', 'quebra', 'mapa_retorno_atendidos',
                  'mapa_retorno_nao_atendidos', 'extensao_retorno_itens_atendidos',
                  'extensao_retorno_itens_nao_atendidos', 'mascara_retorno_atendidos', 'mascara_retorno_nao_atendidos',
                  'sobrepoe_arquivo', 'mapa_retorno_nf', 'mascara_nf', 'extensao_nf', 'sobrepoe_nf',
                  'usuario_arquivo_preco', 'mascara_remessa_arq_preco', 'move_arq_preco', 'diretorio_arq_preco']
