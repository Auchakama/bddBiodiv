# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-15 09:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bddapp', '0015_answerdata_something'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answerdata',
            name='something',
        ),
    ]
