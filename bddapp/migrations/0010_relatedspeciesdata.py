# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-14 15:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bddapp', '0009_auto_20170614_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedSpeciesData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CDN_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='something', to='bddapp.SpeciesData')),
                ('relatedSpecies', models.ManyToManyField(to='bddapp.SpeciesData')),
            ],
        ),
    ]
