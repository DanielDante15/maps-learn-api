# Generated by Django 4.1.7 on 2023-11-01 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_motorista_options_alter_motorista_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='motorista',
            name='nome',
        ),
    ]
