# Generated by Django 4.0.5 on 2022-06-07 22:09

from django.db import migrations, models
import django.db.models.deletion
import django_cpf_cnpj.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', django_cpf_cnpj.fields.CNPJField(max_length=18)),
                ('telefone', models.CharField(max_length=24)),
                ('nome', models.CharField(max_length=96)),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('endereco', models.CharField(max_length=96)),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='data de cadastro')),
            ],
        ),
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
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='data de cadastro')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoriaitem')),
            ],
        ),
        migrations.CreateModel(
            name='Movimentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('justificativa', models.TextField(blank=True, max_length=96, null=True)),
                ('idFamilia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.familia')),
            ],
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=96)),
                ('cpf', django_cpf_cnpj.fields.CPFField(max_length=14)),
                ('endereco', models.CharField(max_length=96)),
                ('observacao', models.TextField(blank=True, max_length=96, null=True)),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='data de cadastro')),
                ('idEntidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.entidade')),
            ],
        ),
        migrations.CreateModel(
            name='MovimentosItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='data de cadastro')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.item')),
                ('movimentos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.movimentos')),
            ],
        ),
        migrations.AddField(
            model_name='movimentos',
            name='representante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.representante'),
        ),
        migrations.CreateModel(
            name='IntegranteFamilia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=96)),
                ('cpf', django_cpf_cnpj.fields.CPFField(max_length=14)),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='data de cadastro')),
                ('familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.familia')),
            ],
        ),
    ]
