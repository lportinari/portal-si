# Generated by Django 3.0 on 2020-02-17 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criacão')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de Modificação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('codigo_cliente', models.CharField(max_length=100, unique=True, verbose_name='Código do cliente')),
                ('mapa', models.CharField(choices=[('Angeloni', 'Angeloni'), ('Catarinensecialatino', 'Catarinensecialatino'), ('Consys3', 'Consys3'), ('Consys8', 'Consys8'), ('Cooper', 'Cooper'), ('Drogal', 'Drogal'), ('EDM2', 'EDM2'), ('Eurofarma2', 'Eurofarma2'), ('Eurofarma3', 'Eurofarma3'), ('Farma01', 'Farma01'), ('Febrafar', 'Febrafar'), ('Fidelize2', 'Fidelize2'), ('Gestao40', 'Gestao40'), ('Mantercorp', 'Mantercorp'), ('Mercanet', 'Mercanet'), ('Nissei', 'Nissei'), ('PanarelloCli', 'PanarelloCli'), ('PanarelloExt2', 'PanarelloExt2'), ('PanarelloExt3', 'PanarelloExt3'), ('PdvLink', 'PdvLink'), ('PedPoa', 'PedPoa'), ('Permanente', 'Permanente'), ('Pharmalink', 'Pharmalink'), ('Pharmalink11', 'Pharmalink11'), ('Pharmalink3', 'Pharmalink3'), ('PharmalinkFidelize', 'PharmalinkFidelize'), ('Prodoctor', 'Prodoctor'), ('Rosario', 'Rosario'), ('Rosario01', 'Rosario01'), ('Rosario02', 'Rosario02'), ('SantaCruz4', 'SantaCruz4'), ('SantaCruz5', 'SantaCruz5'), ('Sintegra2', 'Sintegra2'), ('Sudestefarma', 'Sudestefarma')], default='', max_length=100, verbose_name='Mapa')),
                ('van', models.CharField(choices=[('BRAIR', 'BRAIR'), ('ENTIRE', 'ENTIRE'), ('ENTIRESI', 'ENTIRESI'), ('EPHARMA', 'EPHARMA'), ('FEBRAFAR', 'FEBRAFAR'), ('Fidelize', 'Fidelize'), ('FIDELIZE', 'FIDELIZE'), ('FOCOPDV', 'FOCOPDV'), ('IMS', 'IMS'), ('MERCANET', 'MERCANET'), ('MOST', 'MOST'), ('NISSEI', 'NISSEI'), ('ORIZON', 'ORIZON'), ('PHARMALINK', 'PHARMALINK'), ('PRODOCTOR', 'PRODOCTOR'), ('RAIA', 'RAIA'), ('RUNN', 'RUNN'), ('VIDALINK', 'VIDALINK'), ('VISAO', 'VISAO')], default='BRAIR', max_length=100, verbose_name='Van')),
                ('apontador', models.CharField(max_length=100, verbose_name='Apontador')),
                ('quebra', models.CharField(choices=[('', ''), ('Sim', 'Sim'), ('Não', 'Não')], default='', max_length=20, verbose_name='Quebra')),
                ('mapa_retorno_atendidos', models.CharField(choices=[('', ''), ('Drogal_Atendidos', 'Drogal_Atendidos'), ('Drogal_Atendidos_Contabiliza', 'Drogal_Atendidos_Contabiliza'), ('EDM2', 'EDM2'), ('Fidelize2', 'Fidelize2'), ('PanarelloCli_Atendidos', 'PanarelloCli_Atendidos'), ('PanarelloExt2_Atendidos', 'PanarelloExt2_Atendidos'), ('PdvLink', 'PdvLink'), ('PanarelloExt3_Atendidos', 'PanarelloExt3_Atendidos'), ('PharmalinkFidelize', 'PharmalinkFidelize'), ('Pharmalink3', 'Pharmalink3'), ('Pharmalink11', 'Pharmalink11'), ('PedPoa_Atendidos', 'PedPoa_Atendidos'), ('Permanente', 'Permanente'), ('Rosario_Atendidos', 'Rosario_Atendidos'), ('Rosario01', 'Rosario01'), ('Rosario02', 'Rosario02'), ('Rosario_Atendidos_Contabiliza', 'Rosario_Atendidos_Contabiliza'), ('SantaCruz5', 'SantaCruz5'), ('Sudestefarma_Atendidos', 'Sudestefarma_Atendidos'), ('Sintegra2', 'Sintegra2')], max_length=100)),
                ('mapa_retorno_nao_atendidos', models.CharField(choices=[('', ''), ('Drogal_NaoAtendidos', 'Drogal_NaoAtendidos'), ('Drogal_NaoAtendidos_Contabiliza', 'Drogal_NaoAtendidos_Contabiliza'), ('EDM2', 'EDM2'), ('PanarelloCli_NaoAtendidos', 'PanarelloCli_NaoAtendidos'), ('PanarelloExt2_NaoAtendidos', 'PanarelloExt2_NaoAtendidos'), ('PanarelloExt3_NaoAtendidos', 'PanarelloExt3_NaoAtendidos'), ('PedPoa_NaoAtendidos', 'PedPoa_NaoAtendidos'), ('Permanente', 'Permanente'), ('PdvLink', 'PdvLink'), ('Pharmalink11', 'Pharmalink11'), ('Rosario_NaoAtendidos', 'Rosario_NaoAtendidos'), ('Rosario02', 'Rosario02'), ('Rosario_NaoAtendidos_Contabiliza', 'Rosario_NaoAtendidos_Contabiliza'), ('SantaCruz5', 'SantaCruz5'), ('Sudestefarma_NaoAtendidos', 'Sudestefarma_NaoAtendidos'), ('Sintegra2', 'Sintegra2')], max_length=100)),
                ('extensao_retorno_itens_atendidos', models.CharField(choices=[('', ''), ('fal', 'fal'), ('not', 'not'), ('ret', 'ret'), ('txt', 'txt')], max_length=10)),
                ('extensao_retorno_itens_nao_atendidos', models.CharField(choices=[('', ''), ('fal', 'fal'), ('not', 'not'), ('ret', 'ret'), ('txt', 'txt')], max_length=10)),
                ('mascara_retorno_atendidos', models.CharField(max_length=100)),
                ('mascara_retorno_nao_atendidos', models.CharField(max_length=100)),
                ('sobrepoe_arquivo', models.CharField(choices=[('', ''), ('Sim', 'Sim'), ('Não', 'Não')], max_length=10, verbose_name='Sobrepõe arquivo?')),
                ('mapa_retorno_nf', models.CharField(choices=[('', ''), ('Eurofarma2', 'Eurofarma2'), ('Fidelize2', 'Fidelize2'), ('Focopdv', 'Focopdv'), ('Mantercorp', 'Mantercorp'), ('Mercanet', 'Mercanet'), ('PanarelloExt2', 'PanarelloExt2'), ('Pharmalink', 'Pharmalink'), ('Pharmalink11', 'Pharmalink11'), ('Pharmalink3', 'Pharmalink3'), ('PharmalinkFidelize', 'PharmalinkFidelize'), ('Phl', 'Phl'), ('Prodoctor', 'Prodoctor'), ('Running', 'Running')], max_length=100)),
                ('mascara_nf', models.CharField(max_length=100, verbose_name='Máscara Nota Fiscal')),
                ('extensao_nf', models.CharField(choices=[('', ''), ('nfs', 'nfs'), ('not', 'not'), ('txt', 'txt')], max_length=10, verbose_name='Extensão Nota Fiscal')),
                ('sobrepoe_nf', models.BooleanField(choices=[('', ''), ('Sim', 'Sim'), ('Não', 'Não')], verbose_name='Sobrepões NF?')),
                ('usuario_arquivo_preco', models.CharField(max_length=100)),
                ('mascara_remessa_arq_preco', models.CharField(max_length=100, verbose_name='Máscara Remessa ARQ Preço')),
                ('move_arq_preco', models.BooleanField(choices=[('', ''), ('Sim', 'Sim'), ('Não', 'Não')], verbose_name='Move ARQ preço?')),
                ('diretorio_arq_preco', models.CharField(max_length=100, verbose_name='Diretório ARQ Preço')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsuariosPanHomol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criacão')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de Modificação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('codigo_cliente', models.CharField(max_length=100, unique=True, verbose_name='Código do cliente')),
                ('mapa', models.CharField(max_length=100)),
                ('van', models.CharField(max_length=100)),
                ('apontador', models.CharField(max_length=100, verbose_name='Informe o apontador')),
                ('quebra', models.CharField(max_length=10)),
                ('mapa_retorno_atendidos', models.CharField(max_length=100)),
                ('mapa_retorno_nao_atendidos', models.CharField(max_length=100)),
                ('extensao_retorno_itens_atendidos', models.CharField(max_length=100)),
                ('extensao_retorno_itens_nao_atendidos', models.CharField(max_length=100)),
                ('mascara_retorno_atendidos', models.CharField(max_length=100)),
                ('mascara_retorno_nao_atendidos', models.CharField(max_length=100)),
                ('sobrepoe_arquivo', models.CharField(max_length=10)),
                ('mapa_retorno_nf', models.CharField(max_length=100)),
                ('mascara_nf', models.CharField(max_length=100)),
                ('extensao_nf', models.CharField(max_length=10)),
                ('sobrepoe_nf', models.BooleanField()),
                ('usuario_arquivo_preco', models.CharField(max_length=100)),
                ('mascara_remessa_arq_preco', models.CharField(max_length=100)),
                ('move_arq_preco', models.BooleanField()),
                ('diretorio_arq_preco', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
