# Generated by Django 4.1.2 on 2022-10-23 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('familias', '0001_initial'),
        ('grupos', '0001_initial'),
        ('itens', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('justificativa', models.TextField(blank=True, max_length=96, null=True)),
                ('idFamilia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='familias.familia')),
                ('representante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='grupos.representante')),
            ],
        ),
        migrations.CreateModel(
            name='MovimentosItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='data de cadastro')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itens.item')),
                ('movimentos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doacoes.movimentos')),
            ],
        ),
    ]
