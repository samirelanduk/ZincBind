# Generated by Django 2.2 on 2019-06-14 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190612_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chaincluster',
            name='id',
            field=models.CharField(max_length=128, primary_key=True, serialize=False),
        ),
    ]
