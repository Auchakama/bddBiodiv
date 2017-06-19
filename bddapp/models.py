from __future__ import unicode_literals
from django.db import models

class LargeSpeciesCategoryData(models.Model):
    
    largeCategoryName = models.CharField(max_length=100)
    largeDetailledCategoryName = models.TextField(blank=True)
    largeCategoryPictoUrl = models.URLField()
    
    def __unicode__(self):
        
        return self.largeCategoryName

class PreciseSpeciesCategoryData(models.Model):
    
    preciseCategoryName = models.CharField(max_length=100)
    preciseDetailledCategoryName = models.TextField(blank=True)
    preciseCategoryPictoUrl = models.URLField()
    trysomething = models.CharField(max_length=50)
    
    def __unicode__(self):
        
        return self.preciseCategoryName

class HabitatData(models.Model):
    
    habitatName = models.CharField(max_length=100)
    detailledHabitatName = models.TextField(blank=True)
    habitatPictoUrl = models.URLField()
    
    def __unicode__(self):
        
        return self.habitatName

class DifficultyData(models.Model):
    
    difficulty = models.CharField(max_length=50)
    
    def __unicode__(self):
        
        return self.difficulty

class SizeCompareData(models.Model):
    
    sizeCompare = models.CharField(max_length=50)
    
    def __unicode__(self):
        
        return self.sizeCompare

class SpeciesData(models.Model):
    
    CDN_name = models.IntegerField(primary_key=True)
    vernacularName = models.CharField(max_length=100)
    scientificName = models.CharField(max_length=100)
    shortDescription = models.TextField()
    longDescription = models.TextField()
    funFact = models.TextField(blank=True)
    mainPhotoUrl = models.URLField()
    sketchPhotoUrl = models.URLField()
    silhouettePhotoUrl = models.URLField()
    inpnLink = models.URLField()
    telabotanicaLink = models.URLField(blank=True)
    sizeCompare = models.ForeignKey(SizeCompareData)
    minSizeInCm = models.IntegerField()
    maxSizeInCm = models.IntegerField()
    presentInSpring = models.BooleanField()
    presentInSummer = models.BooleanField()
    presentInAutumn = models.BooleanField()
    presentInWinter = models.BooleanField()
    habitatDescription = models.TextField()
    presentIn30_Gard = models.BooleanField()
    presentIn34_Herault = models.BooleanField()
    presentIn48_Lozere = models.BooleanField()
    presentIn11_Aude = models.BooleanField()
    presentIn66_PyreneesOrientales = models.BooleanField()
    geographicalSpread = models.CharField(max_length=100, blank=True)
    largeCategoryName = models.ForeignKey(LargeSpeciesCategoryData)
    preciseCategoryName = models.ForeignKey(PreciseSpeciesCategoryData)
    habitatName = models.ManyToManyField(HabitatData)

    def __unicode__(self):

        return str (self.CDN_name)


class MorphologyData(models.Model):
    
    CDN_name = models.ForeignKey(SpeciesData)
    morphologyDescription = models.CharField(max_length=250)
    morphologyImageUrl = models.URLField()
    
    def __unicode__(self):
        
        return self.morphologyDescription

class SpeciesPhotoData(models.Model):
    
    CDN_name = models.ForeignKey(SpeciesData)
    speciesPhotoUrl = models.URLField()
    
    def __unicode__(self):
        
        return self.speciesPhotoUrl

class ChallengeData(models.Model):
    
    challengeName = models.CharField(max_length=100)
    CDN_name = models.ForeignKey(SpeciesData)
    instructions = models.CharField(max_length=100)
    noOfObservationsRequired = models.IntegerField()
    rewardInXP = models.DecimalField(max_digits=15, decimal_places=10)
    difficulty = models.ForeignKey(DifficultyData)
    sponsored = models.BooleanField()
    logo = models.URLField()
    geoloc = models.CharField(max_length=100)
    
    def __unicode__(self):
        
        return self.challengeName


class QuestionData(models.Model):
    
    idChallenge = models.ForeignKey(ChallengeData)
    questionText = models.CharField(max_length=250)
    questionImageUrl = models.URLField()
    
    def __unicode__(self):
        
        return self.questionText

class AnswerData(models.Model):
    
    idChallenge = models.ForeignKey(ChallengeData)
    idQuestion = models.ForeignKey(QuestionData)
    isGoodAnswer = models.BooleanField()
    answerText = models.CharField(max_length=250)
    answerImageUrl = models.URLField()
    po_number = models.TextField()

    def __unicode__(self):
    
        return self.answerText

class RelatedSpeciesData(models.Model):
    
    CDN_name = models.ForeignKey(SpeciesData, related_name='Species')
    relatedSpecies = models.ManyToManyField(SpeciesData)
    
    def __unicode__(self):
        
        return self.relatedSpecies

class SpeciesCategoryData(models.Model):
    
    CDN_name = models.ForeignKey(SpeciesData)
    categoryName = models.CharField(max_length=100)
    detailledCategoryName = models.CharField(max_length=250)
    categoryPictoUrl = models.URLField()
    
    def __unicode__(self):
        
        return self.categoryName

class IndicesSpeciesData(models.Model):

    CDN_name = models.ForeignKey(SpeciesData)
    indicesSpecies = models.TextField()

    def __unicode__(self):
    
        return self.indicesSpecies
