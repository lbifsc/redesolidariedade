# Generated by Django 3.2.15 on 2022-09-04 19:50

from django.db import migrations, models
import django.db.models.deletion
import django_cpf_cnpj.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeChefeFamilia', models.CharField(max_length=96)),
                ('cpfChefeFamilia', django_cpf_cnpj.fields.CPFField(max_length=14)),
                ('enderecoChefeFamilia', models.CharField(max_length=96)),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='data de cadastro')),
            ],
        ),
        migrations.CreateModel(
            name='IntegranteFamilia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=96)),
                ('cpf', django_cpf_cnpj.fields.CPFField(max_length=14)),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='data de cadastro')),
                ('familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='familias.familia')),
            ],
        ),
    ]