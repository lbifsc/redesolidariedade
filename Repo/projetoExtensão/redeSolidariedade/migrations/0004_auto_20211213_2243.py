# Generated by Django 2.2.24 on 2021-12-14 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redeSolidariedade', '0003_auto_20211213_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='categoria',
            field=models.CharField(blank=True, choices=[(1, 'Alimento Não Perecível'), (2, 'Remédio'), (3, 'Protetor Solar')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='descricao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
