# Generated by Django 4.1.7 on 2023-03-16 18:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_empresa_endereco'),
    ]

    operations = [
        migrations.AddField(
            model_name='motorista',
            name='empresa',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
