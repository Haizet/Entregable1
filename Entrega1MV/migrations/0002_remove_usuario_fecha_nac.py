# Generated by Django 4.1.1 on 2022-09-06 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Entrega1MV', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='fecha_nac',
        ),
    ]