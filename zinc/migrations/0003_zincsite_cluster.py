# Generated by Django 2.0.2 on 2018-06-09 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zinc', '0002_chain_cluster'),
    ]

    operations = [
        migrations.AddField(
            model_name='zincsite',
            name='cluster',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]