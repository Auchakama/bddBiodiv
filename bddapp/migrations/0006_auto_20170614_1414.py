# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-14 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bddapp', '0005_auto_20170614_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speciesdata',
            name='habitatName',
        ),
        migrations.AddField(
            model_name='speciesdata',
            name='habitatName',
            field=models.ManyToManyField(to='bddapp.HabitatData'),
        ),
    ]