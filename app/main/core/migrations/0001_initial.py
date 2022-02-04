# Generated by Django 4.0.1 on 2022-01-29 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(blank=True, max_length=24, null=True)),
                ('nome', models.CharField(blank=True, max_length=96, null=True)),
                ('telefone', models.CharField(blank=True, max_length=24, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('endereco', models.CharField(blank=True, max_length=96, null=True)),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='data de cadastro')),
            ],
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeChefeFamilia', models.CharField(blank=True, max_length=96, null=True)),
                ('cpfChefeFamilia', models.CharField(blank=True, max_length=24, null=True)),
                ('enderecoChefeFamilia', models.CharField(blank=True, max_length=96, null=True)),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='data de cadastro')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, max_length=100, null=True)),
                ('categoria', models.CharField(blank=True, choices=[('1', 'Alimento Não Perecível'), ('2', 'Remédio'), ('3', 'Protetor Solar')], max_length=50, null=True)),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='data de cadastro')),
            ],
        ),
        migrations.CreateModel(
            name='Movimentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True, null=True)),
                ('justificativa', models.TextField(blank=True, max_length=96, null=True)),
                ('idFamilia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.familia')),
            ],
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=96, null=True)),
                ('cpf', models.CharField(blank=True, max_length=24, null=True)),
                ('endereco', models.CharField(blank=True, max_length=96, null=True)),
                ('obsercacao', models.TextField(blank=True, max_length=96, null=True)),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='data de cadastro')),
                ('idEntidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.entidade')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(blank=True, max_length=100, null=True)),
                ('senha', models.CharField(blank=True, max_length=100, null=True)),
                ('papel', models.CharField(blank=True, choices=[('a', 'Admin'), ('b', 'User')], max_length=2, null=True)),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='data de cadastro')),
                ('representante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.representante')),
            ],
        ),
        migrations.CreateModel(
            name='MovimentosItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='data de cadastro')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.item')),
                ('movimentos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.movimentos')),
            ],
        ),
        migrations.CreateModel(
            name='IntegranteFamilia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=96, null=True)),
                ('cpf', models.CharField(blank=True, max_length=24, null=True)),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='data de cadastro')),
                ('Familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.familia')),
            ],
        ),
    ]
