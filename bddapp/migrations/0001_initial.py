# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-14 08:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isGoodAnswer', models.BooleanField()),
                ('answerText', models.CharField(max_length=250)),
                ('answerImageUrl', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ChallengeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challengeName', models.CharField(max_length=100)),
                ('instructions', models.CharField(max_length=100)),
                ('noOfObservationsRequired', models.IntegerField()),
                ('rewardInXP', models.DecimalField(decimal_places=10, max_digits=15)),
                ('difficulty', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HabitatData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habitatName', models.CharField(max_length=100)),
                ('detailledHabitatName', models.TextField()),
                ('habitatPictoUrl', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='MorphologyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('morphologyDescription', models.CharField(max_length=250)),
                ('morphologyImageUrl', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='QuestionData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionText', models.CharField(max_length=250)),
                ('questionImageUrl', models.URLField()),
                ('idChallenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bddapp.ChallengeData')),
            ],
        ),
        migrations.CreateModel(
            name='SpeciesCategoryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=100)),
                ('detailledCategoryName', models.CharField(max_length=250)),
                ('categoryPictoUrl', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='SpeciesData',
            fields=[
                ('CDN_name', models.IntegerField(primary_key=True, serialize=False)),
                ('vernacularName', models.CharField(max_length=100)),
                ('scientificName', models.CharField(max_length=100)),
                ('shortDescription', models.TextField()),
                ('longDescription', models.TextField()),
                ('funFact', models.TextField(blank=True)),
                ('mainPhotoUrl', models.URLField()),
                ('sketchPhotoUrl', models.URLField()),
                ('silhouettePhotoUrl', models.URLField()),
                ('inpnLink', models.URLField()),
                ('telabotanicaLink', models.URLField(blank=True)),
                ('sizeCompare', models.CharField(max_length=100)),
                ('minSizeInCm', models.IntegerField()),
                ('maxSizeInCm', models.IntegerField()),
                ('presentInSpring', models.BooleanField()),
                ('presentInSummer', models.BooleanField()),
                ('presentInAutumn', models.BooleanField()),
                ('presentInWinter', models.BooleanField()),
                ('habitatDescription', models.TextField()),
                ('presentIn30_Gard', models.BooleanField()),
                ('presentIn34_Herault', models.BooleanField()),
                ('presentIn48_Lozere', models.BooleanField()),
                ('presentIn11_Aude', models.BooleanField()),
                ('presentIn66_PyreneesOrientales', models.BooleanField()),
                ('geographicalSpread', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SpeciesPhotoData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciesPhotoUrl', models.URLField()),
                ('CDN_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bddapp.SpeciesData')),
            ],
        ),
        migrations.AddField(
            model_name='speciescategorydata',
            name='CDN_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bddapp.SpeciesData'),
        ),
        migrations.AddField(
            model_name='morphologydata',
            name='CDN_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bddapp.SpeciesData'),
        ),
        migrations.AddField(
            model_name='habitatdata',
            name='CDN_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bddapp.SpeciesData'),
        ),
        migrations.AddField(
            model_name='challengedata',
            name='CDN_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bddapp.SpeciesData'),
        ),
        migrations.AddField(
            model_name='answerdata',
            name='idChallenge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bddapp.ChallengeData'),
        ),
        migrations.AddField(
            model_name='answerdata',
            name='idQuestion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bddapp.QuestionData'),
        ),
    ]
