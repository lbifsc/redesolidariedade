# Generated by Django 2.2.24 on 2021-12-14 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redeSolidariedade', '0004_auto_20211213_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='categoria',
            field=models.CharField(blank=True, choices=[('1', 'Alimento Não Perecível'), ('2', 'Remédio'), ('3', 'Protetor Solar')], max_length=50, null=True),
        ),
    ]
