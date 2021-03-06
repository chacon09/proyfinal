# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 05:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deportes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Deportista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Participacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deportes.Deporte')),
                ('deportista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deportes.Deportista')),
            ],
        ),
        migrations.RemoveField(
            model_name='actuacion',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='actuacion',
            name='pelicula',
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='actores',
        ),
        migrations.DeleteModel(
            name='Actor',
        ),
        migrations.DeleteModel(
            name='Actuacion',
        ),
        migrations.DeleteModel(
            name='Pelicula',
        ),
        migrations.AddField(
            model_name='deportista',
            name='deportes',
            field=models.ManyToManyField(through='deportes.Participacion', to='deportes.Deporte'),
        ),
    ]
