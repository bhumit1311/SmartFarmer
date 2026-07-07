from django.contrib import admin
from .models import Crop, DiseasePrediction, CropLibrary, FertilizerRecommendation, FarmingNews

@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ('name', 'variety', 'farmer', 'land_size', 'status', 'sowing_date')
    list_filter = ('status', 'name')
    search_fields = ('variety', 'farmer__username')

@admin.register(DiseasePrediction)
class DiseasePredictionAdmin(admin.ModelAdmin):
    list_display = ('crop_name', 'farmer', 'disease', 'confidence', 'created_at')

@admin.register(CropLibrary)
class CropLibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'gujarati_name', 'season')

@admin.register(FertilizerRecommendation)
class FertilizerRecommendationAdmin(admin.ModelAdmin):
    list_display = ('crop_name', 'farmer', 'fertilizer_name', 'crop_stage')

@admin.register(FarmingNews)
class FarmingNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'source_name', 'pub_date')
