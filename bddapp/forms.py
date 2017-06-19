#!/usr/bin/env python
#-*- coding: utf-8 -*-

from django import forms
from .models import *

class SpeciesDataForm(forms.ModelForm):
    class Meta:
        model = SpeciesData
        fields = '__all__'

class HabitatDataForm(forms.ModelForm):
    class Meta:
        model = HabitatData
        fields = '__all__'

class MorphologyDataForm(forms.ModelForm):
    class Meta:
        model = MorphologyData
        fields = '__all__'

class SpeciesCategoryDataForm(forms.ModelForm):
    class Meta:
        model = SpeciesCategoryData
        fields = '__all__'

class SpeciesPhotoDataForm(forms.ModelForm):
    class Meta:
        model = SpeciesPhotoData
        fields = '__all__'

class ChallengeDataForm(forms.ModelForm):
    class Meta:
        model = ChallengeData
        fields = '__all__'

class QuestionDataForm(forms.ModelForm):
    class Meta:
        model = QuestionData
        fields = '__all__'

class AnswerDataForm(forms.ModelForm):
    class Meta:
        model = AnswerData
        fields = '__all__'

class RelatedSpeciesDataForm(forms.ModelForm):
    class Meta:
        model = RelatedSpeciesData
        fields = '__all__'

