# Generated by Django 4.0.4 on 2022-06-23 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mercado', '0004_itensatendimentorascunho_solidarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='itensatendimento',
            name='produto',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
    ]
