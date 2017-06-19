from django.contrib import admin
from .models import *
from .forms import *


class RelatedSpeciesDataAdmin(admin.ModelAdmin):

    list_display   = ('CDN_name', )
    list_filter    = ()
    ordering       = ()
    search_fields  = ()
    fields = ('CDN_name', 'relatedSpecies')

class LargeSpeciesCategoryDataAdmin(admin.ModelAdmin):
    
    list_display   = ('largeCategoryName', 'largeDetailledCategoryName')
    list_filter    = ()
    ordering       = ()
    search_fields  = ('largeCategoryName', )
    fields = ('largeCategoryName', 'largeDetailledCategoryName', 'largeCategoryPictoUrl')

class PreciseSpeciesCategoryDataAdmin(admin.ModelAdmin):
    
    list_display   = ('preciseCategoryName', 'preciseDetailledCategoryName')
    list_filter    = ()
    ordering       = ()
    search_fields  = ('preciseCategoryName', )
    fields = ('preciseCategoryName', 'preciseDetailledCategoryName', 'preciseCategoryPictoUrl')

class SpeciesDataAdmin(admin.ModelAdmin):
    
    list_display   = ('CDN_name', 'vernacularName', 'scientificName', 'shortDescription')
    list_filter    = ()
    ordering       = ('CDN_name', )
    search_fields  = ('CDN_name', 'vernacularName', 'scientificName', 'minSizeInCm', 'maxSizeInCm')
    fields = ('CDN_name', 'vernacularName', 'scientificName', 'shortDescription', 'longDescription', 'funFact', 'mainPhotoUrl', 'sketchPhotoUrl', 'silhouettePhotoUrl', 'inpnLink', 'telabotanicaLink', 'sizeCompare', 'minSizeInCm', 'maxSizeInCm', 'presentInSpring', 'presentInSummer', 'presentInAutumn', 'presentInWinter', 'habitatDescription', 'presentIn30_Gard', 'presentIn34_Herault', 'presentIn48_Lozere', 'presentIn11_Aude', 'presentIn66_PyreneesOrientales', 'geographicalSpread', 'largeCategoryName', 'preciseCategoryName', 'habitatName')
    class Media:
        js = ('js/admin/mymodel.js',)


class HabitatDataAdmin(admin.ModelAdmin):
    
    list_display   = ('habitatName', 'detailledHabitatName')
    list_filter    = ('habitatName', )
    ordering       = ()
    search_fields  = ('habitatName', )
    fields = ('habitatName', 'detailledHabitatName', 'habitatPictoUrl')


class MorphologyDataAdmin(admin.ModelAdmin):
    
    list_display   = ('CDN_name', 'morphologyDescription')
    list_filter    = ()
    ordering       = ()
    search_fields  = ('CDN_name', )
    fields = ('morphologyDescription', 'morphologyImageUrl', 'CDN_name')

class SpeciesPhotoDataAdmin(admin.ModelAdmin):
    
    list_display   = ('CDN_name', 'speciesPhotoUrl')
    list_filter    = ()
    ordering       = ()
    search_fields  = ()
    fields = ('speciesPhotoUrl', 'CDN_name')

class ChallengeDataAdmin(admin.ModelAdmin):
    
    list_display   = ('challengeName', 'difficulty', 'rewardInXP', 'instructions')
    list_filter    = ('difficulty', )
    ordering       = ()
    search_fields  = ('challengeName', 'difficulty', 'rewardInXP')
    fields = ('sponsored', 'challengeName', 'instructions', 'logo', 'geoloc', 'noOfObservationsRequired', 'rewardInXP', 'difficulty', 'CDN_name')

class QuestionDataAdmin(admin.ModelAdmin):
    
    list_display   = ('idChallenge', 'questionText')
    list_filter    = ()
    ordering       = ()
    search_fields  = ()
    fields = ('questionText', 'questionImageUrl', 'idChallenge')

class AnswerDataAdmin(admin.ModelAdmin):
    
    list_display   = ('idChallenge', 'idQuestion', 'isGoodAnswer')
    list_filter    = ()
    ordering       = ()
    search_fields  = ()
    fields = ('isGoodAnswer', 'answerText', 'answerImageUrl', 'idChallenge', 'idQuestion')

class DifficultyDataAdmin(admin.ModelAdmin):

    list_display   = ('difficulty', )
    list_filter    = ()
    ordering       = ()
    search_fields  = ()
    fields = ('difficulty', )

class SizeCompareDataAdmin(admin.ModelAdmin):
    
    list_display   = ('sizeCompare', )
    list_filter    = ()
    ordering       = ()
    search_fields  = ()
    fields = ('sizeCompare', )

class IndicesSpeciesDataAdmin(admin.ModelAdmin):
    
    list_display   = ('CDN_name', 'indicesSpecies' )
    list_filter    = ()
    ordering       = ()
    search_fields  = ()
    fields = ('CDN_name', 'indicesSpecies')


admin.site.register(SpeciesData, SpeciesDataAdmin)
admin.site.register(HabitatData, HabitatDataAdmin)
admin.site.register(MorphologyData, MorphologyDataAdmin)
admin.site.register(LargeSpeciesCategoryData, LargeSpeciesCategoryDataAdmin)
admin.site.register(PreciseSpeciesCategoryData, PreciseSpeciesCategoryDataAdmin)
admin.site.register(SpeciesPhotoData, SpeciesPhotoDataAdmin)
admin.site.register(ChallengeData, ChallengeDataAdmin)
admin.site.register(QuestionData, QuestionDataAdmin)
admin.site.register(AnswerData, AnswerDataAdmin)
admin.site.register(DifficultyData, DifficultyDataAdmin)
admin.site.register(SizeCompareData, SizeCompareDataAdmin)
admin.site.register(RelatedSpeciesData, RelatedSpeciesDataAdmin)
admin.site.register(IndicesSpeciesData, IndicesSpeciesDataAdmin)

