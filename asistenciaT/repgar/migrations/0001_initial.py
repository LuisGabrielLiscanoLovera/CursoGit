# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-13 12:23
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosTecnico',
            fields=[
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('sexo', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer'), ('O', 'Otro')], max_length=1)),
                ('Telefono', models.CharField(max_length=11)),
                ('correo_corporativo', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=11)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=16)),
                ('fecha', models.DateField()),
                ('historico', ckeditor.fields.RichTextField()),
                ('estado', models.CharField(choices=[('R', 'REPARADO'), ('C', 'CAMBIO')], max_length=1)),
                ('tecnico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='repgar.DatosTecnico')),
            ],
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('serial', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('pantalla', models.BooleanField()),
                ('lector', models.BooleanField()),
                ('memoria_ram', models.BooleanField()),
                ('fan_cooler', models.BooleanField(verbose_name='ventilador')),
                ('computadora', models.BooleanField()),
                ('ele', models.BooleanField(verbose_name='Soket de alimentacion')),
                ('tecnico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='repgar.DatosTecnico')),
            ],
        ),
    ]
