# Generated by Django 5.0.4 on 2024-05-23 21:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clase', '0002_rename_ejercicio_ejerciciocategoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='ejerciciocategoria',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='ejerciciocategoria',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='ejercicios/'),
        ),
        migrations.AddField(
            model_name='solucion',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='solucion',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='soluciones/'),
        ),
    ]
