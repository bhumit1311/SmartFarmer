from django.contrib import admin
from .models import UserProfile, WeatherHistory, MandiPrice

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'state', 'primary_crop')

@admin.register(WeatherHistory)
class WeatherHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'query_location', 'temperature', 'condition', 'searched_at')
    
@admin.register(MandiPrice)
class MandiPriceAdmin(admin.ModelAdmin):
    list_display = ('crop_name', 'mandi_name', 'today_price', 'price_date')
    list_filter = ('crop_name', 'price_date')
