# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-19 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zincbind', '0018_zincsite_contrast'),
    ]

    operations = [
        migrations.AddField(
            model_name='zincsite',
            name='solvation',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]