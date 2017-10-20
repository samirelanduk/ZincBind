# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-20 11:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zincsites', '0005_residue_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atom',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('atom_id', models.IntegerField()),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('z', models.FloatField()),
                ('element', models.TextField()),
                ('name', models.TextField()),
                ('charge', models.FloatField()),
                ('bfactor', models.FloatField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='residue',
            options={'ordering': ['chain', 'number']},
        ),
        migrations.AddField(
            model_name='atom',
            name='residue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zincsites.Residue'),
        ),
    ]
