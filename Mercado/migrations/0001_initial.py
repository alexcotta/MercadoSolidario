# Generated by Django 4.0.4 on 2022-06-11 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('atendente', models.CharField(max_length=50)),
                ('data', models.DateField()),
                ('finalizado', models.BooleanField(default=False)),
                ('solidarios', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='AtendimentoRascunho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('atendente', models.CharField(max_length=50)),
                ('data', models.DateField()),
                ('finalizado', models.BooleanField(default=False)),
                ('solidarios', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='AtendimentoTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Modelo de Atendimento',
                'verbose_name_plural': 'Modelos de Atendimento',
                'ordering': ['tipo'],
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['categoria'],
            },
        ),
        migrations.CreateModel(
            name='CodBarProdSol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_barras', models.BigIntegerField(unique=True, verbose_name='código de barras')),
            ],
            options={
                'verbose_name': 'Código do Produto',
                'verbose_name_plural': 'Códigos dos Produtos',
                'ordering': ['id_produto', 'codigo_barras'],
            },
        ),
        migrations.CreateModel(
            name='FonteDoacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=255, verbose_name='descrição')),
            ],
            options={
                'verbose_name': 'Fonte de Doação',
                'verbose_name_plural': 'Fontes de Doações',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='ProdutoSolidario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('unidade', models.CharField(max_length=20)),
                ('preco_solidario', models.FloatField()),
                ('estoque_minimo', models.IntegerField(default=0)),
                ('max_familia', models.IntegerField(default=0)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Mercado.categoria', verbose_name='categoria')),
            ],
            options={
                'verbose_name': 'Produto Solidário',
                'verbose_name_plural': 'Produtos Solidários',
            },
        ),
        migrations.CreateModel(
            name='ItensAtendimentoTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('id_atendimento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Mercado.atendimentotemplate', verbose_name='modelo de atendimento')),
                ('id_produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Mercado.produtosolidario', verbose_name='produto solidario')),
            ],
            options={
                'verbose_name': 'Itens',
                'verbose_name_plural': 'Modelo de Itens',
                'ordering': ['id_atendimento', 'id_produto'],
            },
        ),
        migrations.CreateModel(
            name='ItensAtendimentoRascunho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('validade', models.DateField()),
                ('id_atendimento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Mercado.atendimentorascunho')),
                ('id_codigo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Mercado.codbarprodsol')),
                ('id_produto', models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='Mercado.produtosolidario')),
            ],
        ),
        migrations.CreateModel(
            name='ItensAtendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('validade', models.DateField()),
                ('id_atendimento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Mercado.atendimento')),
                ('id_codigo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Mercado.codbarprodsol')),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('validade', models.DateField()),
                ('id_codigo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Mercado.codbarprodsol')),
                ('id_fonte', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Mercado.fontedoacao')),
            ],
        ),
        migrations.AddField(
            model_name='codbarprodsol',
            name='id_produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Mercado.produtosolidario', verbose_name='Produto Solidário'),
        ),
    ]