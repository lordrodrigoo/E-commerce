# Generated by Django 5.1.4 on 2025-01-23 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_alter_produto_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing_promocional',
            field=models.FloatField(),
        ),
    ]
