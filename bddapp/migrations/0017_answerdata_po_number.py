# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-15 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bddapp', '0016_remove_answerdata_something'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerdata',
            name='po_number',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
