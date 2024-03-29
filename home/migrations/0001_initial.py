# Generated by Django 4.1.7 on 2023-11-01 19:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('razao_social', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=12, null=True, verbose_name='CEP')),
                ('logradouro', models.CharField(max_length=50, verbose_name='Logradouro')),
                ('complemento', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Compemento')),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro')),
                ('localidade', models.CharField(max_length=20, verbose_name='Localidade')),
                ('uf', models.CharField(max_length=20, verbose_name='UF')),
                ('num_casa', models.CharField(blank=True, max_length=6, null=True, verbose_name='Número')),
                ('latitude', models.FloatField(default=None, max_length=20, null=True)),
                ('longitude', models.FloatField(default=None, max_length=20, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cliente', verbose_name='Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='NotaFiscal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_doc', models.CharField(max_length=50, verbose_name='Numero Documento')),
                ('itens', models.IntegerField(verbose_name='Itens')),
                ('volume', models.IntegerField(verbose_name='Volume')),
                ('redespacho', models.BooleanField()),
                ('end_redespacho', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='home.endereco', verbose_name='Endereço')),
            ],
        ),
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('contato', models.CharField(max_length=15, verbose_name='Contato')),
                ('endereco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home.endereco', verbose_name='Endereço')),
                ('entrega', models.ManyToManyField(blank=True, null=True, related_name='enderecos_entrega', to='home.endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=50, unique=True)),
                ('email', models.CharField(max_length=80, unique=True)),
                ('cnpj', models.CharField(max_length=18, unique=True)),
                ('endereco', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='home.endereco', verbose_name='Endereço')),
                ('motorista', models.ManyToManyField(blank=True, related_name='lista_empresas', to='home.motorista')),
            ],
        ),
    ]
