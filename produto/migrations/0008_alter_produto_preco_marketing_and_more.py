# Generated by Django 5.1.4 on 2025-01-23 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0007_alter_variacao_preco_promocional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing',
            field=models.FloatField(verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing_promocional',
            field=models.FloatField(verbose_name='Preço Promo'),
        ),
    ]
