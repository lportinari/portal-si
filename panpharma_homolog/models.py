from django.db import models


class Base(models.Model):
    criado = models.DateField('Data de Criacão', auto_now_add=True)
    modificado = models.DateField('Data de Modificação', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


MAPA_CHOICES = (
    ('', ''), ('Angeloni', 'Angeloni'), ('Catarinensecialatino', 'Catarinensecialatino'), ('Consys3', 'Consys3'),
    ('Consys8', 'Consys8'), ('Cooper', 'Cooper'), ('Drogal', 'Drogal'), ('EDM2', 'EDM2'), ('Eurofarma2', 'Eurofarma2'),
    ('Eurofarma3', 'Eurofarma3'), ('Farma01', 'Farma01'), ('Febrafar', 'Febrafar'), ('Fidelize2', 'Fidelize2'),
    ('Gestao40', 'Gestao40'), ('Mantercorp', 'Mantercorp'), ('Mercanet', 'Mercanet'), ('Nissei', 'Nissei'),
    ('PanarelloCli', 'PanarelloCli'), ('PanarelloExt2', 'PanarelloExt2'), ('PanarelloExt3', 'PanarelloExt3'),
    ('PdvLink', 'PdvLink'), ('PedPoa', 'PedPoa'), ('Permanente', 'Permanente'), ('Pharmalink', 'Pharmalink'),
    ('Pharmalink11', 'Pharmalink11'), ('Pharmalink3', 'Pharmalink3'), ('PharmalinkFidelize', 'PharmalinkFidelize'),
    ('Prodoctor', 'Prodoctor'), ('Rosario', 'Rosario'), ('Rosario01', 'Rosario01'), ('Rosario02', 'Rosario02'),
    ('SantaCruz4', 'SantaCruz4'), ('SantaCruz5', 'SantaCruz5'), ('Sintegra2', 'Sintegra2'),
    ('Sudestefarma', 'Sudestefarma'),
)

VAN_CHOICES = (
    ('', ''), ('BRAIR', 'BRAIR'), ('ENTIRE', 'ENTIRE'), ('ENTIRESI', 'ENTIRESI'), ('EPHARMA', 'EPHARMA'),
    ('FEBRAFAR', 'FEBRAFAR'), ('Fidelize', 'Fidelize'), ('FIDELIZE', 'FIDELIZE'), ('FOCOPDV', 'FOCOPDV'),
    ('IMS', 'IMS'), ('MERCANET', 'MERCANET'), ('MOST', 'MOST'), ('NISSEI', 'NISSEI'), ('ORIZON', 'ORIZON'),
    ('PHARMALINK', 'PHARMALINK'), ('PRODOCTOR', 'PRODOCTOR'), ('RAIA', 'RAIA'), ('RUNN', 'RUNN'),
    ('VIDALINK', 'VIDALINK'), ('VISAO', 'VISAO'),
)

QUEBRA_CHOICES = (('', ''), ('Sim', 'Sim'), ('Não', 'Não'))

MAPA_RETORNO_ATENDIDOS = (
    ('', ''), ('Drogal_Atendidos','Drogal_Atendidos'), ('Drogal_Atendidos_Contabiliza', 'Drogal_Atendidos_Contabiliza'),
    ('EDM2', 'EDM2'), ('Fidelize2', 'Fidelize2'), ('PanarelloCli_Atendidos', 'PanarelloCli_Atendidos'),
    ('PanarelloExt2_Atendidos', 'PanarelloExt2_Atendidos'), ('PdvLink', 'PdvLink'),
    ('PanarelloExt3_Atendidos', 'PanarelloExt3_Atendidos'), ('PharmalinkFidelize', 'PharmalinkFidelize'),
    ('Pharmalink3', 'Pharmalink3'), ('Pharmalink11', 'Pharmalink11'), ('PedPoa_Atendidos', 'PedPoa_Atendidos'),
    ('Permanente', 'Permanente'), ('Rosario_Atendidos', 'Rosario_Atendidos'), ('Rosario01', 'Rosario01'),
    ('Rosario02', 'Rosario02'), ('Rosario_Atendidos_Contabiliza', 'Rosario_Atendidos_Contabiliza'),
    ('SantaCruz5', 'SantaCruz5'), ('Sudestefarma_Atendidos', 'Sudestefarma_Atendidos'), ('Sintegra2', 'Sintegra2'),
)

MAPA_RETORNO_NAO_ATENDIDOS = (
    ('', ''), ('Drogal_NaoAtendidos','Drogal_NaoAtendidos'),
    ('Drogal_NaoAtendidos_Contabiliza', 'Drogal_NaoAtendidos_Contabiliza'), ('EDM2', 'EDM2'),
    ('PanarelloCli_NaoAtendidos', 'PanarelloCli_NaoAtendidos'),
    ('PanarelloExt2_NaoAtendidos', 'PanarelloExt2_NaoAtendidos'),
    ('PanarelloExt3_NaoAtendidos', 'PanarelloExt3_NaoAtendidos'),
    ('PedPoa_NaoAtendidos', 'PedPoa_NaoAtendidos'), ('Permanente', 'Permanente'), ('PdvLink', 'PdvLink'),
    ('Pharmalink11', 'Pharmalink11'), ('Rosario_NaoAtendidos', 'Rosario_NaoAtendidos'), ('Rosario02', 'Rosario02'),
    ('Rosario_NaoAtendidos_Contabiliza', 'Rosario_NaoAtendidos_Contabiliza'), ('SantaCruz5', 'SantaCruz5'),
    ('Sudestefarma_NaoAtendidos', 'Sudestefarma_NaoAtendidos'), ('Sintegra2', 'Sintegra2'),
)

EXTENCAO = (
    ('', ''), ('fal', 'fal'), ('not', 'not'), ('ret', 'ret'), ('txt', 'txt'),
)

CHOICES = (
    ('', ''), ('Sim', 'Sim'), ('Não', 'Não'),
)

MAPA_RETORNO_NF = (
    ('', ''), ('Eurofarma2', 'Eurofarma2'), ('Fidelize2', 'Fidelize2'), ('Focopdv', 'Focopdv'),
    ('Mantercorp', 'Mantercorp'), ('Mercanet', 'Mercanet'), ('PanarelloExt2', 'PanarelloExt2'),
    ('Pharmalink', 'Pharmalink'), ('Pharmalink11', 'Pharmalink11'), ('Pharmalink3', 'Pharmalink3'),
    ('PharmalinkFidelize', 'PharmalinkFidelize'), ('Phl', 'Phl'), ('Prodoctor', 'Prodoctor'), ('Running', 'Running'),
)

EXTENCAO_NF = (
    ('', ''), ('nfs', 'nfs'), ('not', 'not'), ('txt', 'txt'),
)

CHOICES_BIN = (
    ('', ''), (0, 0), (1, 1),
)


class Teste(Base):
    codigo_cliente = models.CharField('Código do cliente', max_length=100, unique=True)
    mapa = models.CharField('Mapa', max_length=100, choices=MAPA_CHOICES)
    van = models.CharField('Van', max_length=100, choices=VAN_CHOICES)
    apontador = models.CharField('Apontador', max_length=100)
    quebra = models.CharField('Quebra', max_length=20, choices=QUEBRA_CHOICES)
    mapa_retorno_atendidos = models.CharField(max_length=100, choices=MAPA_RETORNO_ATENDIDOS)
    mapa_retorno_nao_atendidos = models.CharField(max_length=100, choices=MAPA_RETORNO_NAO_ATENDIDOS)
    extensao_retorno_itens_atendidos = models.CharField(max_length=10, choices=EXTENCAO)
    extensao_retorno_itens_nao_atendidos = models.CharField(max_length=10, choices=EXTENCAO)
    mascara_retorno_atendidos = models.CharField(max_length=100)
    mascara_retorno_nao_atendidos = models.CharField(max_length=100)
    sobrepoe_arquivo = models.CharField('Sobrepõe arquivo?', max_length=10, choices=CHOICES)
    mapa_retorno_nf = models.CharField(max_length=100, choices=MAPA_RETORNO_NF)
    mascara_nf = models.CharField('Máscara Nota Fiscal', max_length=100)
    extensao_nf = models.CharField('Extensão Nota Fiscal', max_length=10, choices=EXTENCAO_NF)
    sobrepoe_nf = models.BooleanField('Sobrepões NF?', choices=CHOICES_BIN)
    usuario_arquivo_preco = models.CharField('Usuário Arquivo Preço', max_length=100)
    mascara_remessa_arq_preco = models.CharField('Máscara Remessa ARQ Preço', max_length=100)
    move_arq_preco = models.BooleanField('Move ARQ preço?', choices=CHOICES_BIN)
    diretorio_arq_preco = models.CharField('Diretório ARQ Preço', max_length=100)


class UsuariosPanHomol(Base):
    codigo_cliente = models.CharField('Código do cliente', max_length=100, unique=True)
    mapa = models.CharField('Mapa', max_length=100, choices=MAPA_CHOICES)
    van = models.CharField('Van', max_length=100, choices=VAN_CHOICES)
    apontador = models.CharField('Apontador', max_length=100)
    quebra = models.CharField('Quebra', max_length=20, choices=QUEBRA_CHOICES)
    mapa_retorno_atendidos = models.CharField(max_length=100, choices=MAPA_RETORNO_ATENDIDOS)
    mapa_retorno_nao_atendidos = models.CharField(max_length=100, choices=MAPA_RETORNO_NAO_ATENDIDOS)
    extensao_retorno_itens_atendidos = models.CharField(max_length=10, choices=EXTENCAO)
    extensao_retorno_itens_nao_atendidos = models.CharField(max_length=10, choices=EXTENCAO)
    mascara_retorno_atendidos = models.CharField(max_length=100)
    mascara_retorno_nao_atendidos = models.CharField(max_length=100)
    sobrepoe_arquivo = models.CharField('Sobrepõe arquivo?', max_length=10, choices=CHOICES)
    mapa_retorno_nf = models.CharField(max_length=100, choices=MAPA_RETORNO_NF)
    mascara_nf = models.CharField('Máscara Nota Fiscal', max_length=100)
    extensao_nf = models.CharField('Extensão Nota Fiscal', max_length=10, choices=EXTENCAO_NF)
    sobrepoe_nf = models.BooleanField('Sobrepões NF?', choices=CHOICES_BIN)
    usuario_arquivo_preco = models.CharField('Usuário Arquivo Preço', max_length=100)
    mascara_remessa_arq_preco = models.CharField('Máscara Remessa ARQ Preço', max_length=100)
    move_arq_preco = models.BooleanField('Move ARQ preço?', choices=CHOICES_BIN)
    diretorio_arq_preco = models.CharField('Diretório ARQ Preço', max_length=100)


class CodelistsPanHomol(Base):
    codigo_cliente = models.CharField('Usuário a ser cadastrado', max_length=100, unique=True)
    mapa = models.CharField('Mapa', max_length=100, choices=MAPA_CHOICES)
    van = models.CharField('Van', max_length=100, choices=VAN_CHOICES)
    apontador = models.CharField('Apontador', max_length=100)
    quebra = models.CharField('Quebra', max_length=20, choices=QUEBRA_CHOICES)
    mapa_retorno_atendidos = models.CharField(max_length=100, choices=MAPA_RETORNO_ATENDIDOS)
    mapa_retorno_nao_atendidos = models.CharField(max_length=100, choices=MAPA_RETORNO_NAO_ATENDIDOS)
    extensao_retorno_itens_atendidos = models.CharField(max_length=10, choices=EXTENCAO)
    extensao_retorno_itens_nao_atendidos = models.CharField(max_length=10, choices=EXTENCAO)
    mascara_retorno_atendidos = models.CharField(max_length=100)
    mascara_retorno_nao_atendidos = models.CharField(max_length=100)
    sobrepoe_arquivo = models.CharField('Sobrepõe arquivo?', max_length=10, choices=CHOICES)
    mapa_retorno_nf = models.CharField(max_length=100, choices=MAPA_RETORNO_NF)
    mascara_nf = models.CharField('Máscara Nota Fiscal', max_length=100)
    extensao_nf = models.CharField('Extensão Nota Fiscal', max_length=10, choices=EXTENCAO_NF)
    sobrepoe_nf = models.BooleanField('Sobrepões NF?', choices=CHOICES_BIN)
    usuario_arquivo_preco = models.CharField('Usuário Arquivo Preço', max_length=100)
    mascara_remessa_arq_preco = models.CharField('Máscara Remessa ARQ Preço', max_length=100)
    move_arq_preco = models.BooleanField('Move ARQ preço?', choices=CHOICES_BIN)
    diretorio_arq_preco = models.CharField('Diretório ARQ Preço', max_length=100)

    def __str__(self):
        return self.codigo_cliente


