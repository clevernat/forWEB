from django.contrib import admin
from forecasts.models import Map, TemperatureAndRelativeHumidity, SummaryForecast


# class MapAdmin(admin.ModelAdmin):
#     list_display = ('utc_date', 'created')
#     list_display_links = ('utc_date', 'created')
#     list_filter = ('utc_date', 'summary', 'created')
#     # list_editable = ('temp',)
#     search_fields = ('utc_date', 'summary', 'created')
#     list_per_page = 20


# class TemperatureAndRelativeHumidityAdmin(admin.ModelAdmin):
#     list_display = ('utc_date', 'summary', 'created')
#     list_display_links = ('utc_date', 'created')
#     list_filter = ('utc_date', 'summary', 'created')
#     # list_editable = ('temp',)
#     search_fields = ('utc_date', 'created')
#     list_per_page = 20


# class SummaryForecastAdmin(admin.ModelAdmin):
#     list_display = ('utc_date', 'temperature_day',
#                     'temperature_night', 'rain_day', 'rain_night', 'probability_day', 'probability_night', 'relative_humidy_day', 'relative_humidy_night', 'wind_from_day', 'wind_from_night', 'wind_speed_day', 'wind_speed_night', 'wind_gust_day', 'wind_gust_night', 'sunset', 'sunrise', 'created')

#     list_display_links = ('utc_date',)
#     list_filter = ('utc_date', 'temperature_day',
#                    'temperature_night', 'rain_day', 'rain_night', 'probability_day', 'probability_night', 'relative_humidy_day', 'relative_humidy_night', 'wind_from_day', 'wind_from_night', 'wind_speed_day', 'wind_speed_night', 'wind_gust_day', 'wind_gust_night', 'sunset', 'sunrise', 'created')
#     search_fields = ('utc_date', 'temperature_day',
#                      'temperature_night', 'rain_day', 'rain_night', 'probability_day', 'probability_night', 'relative_humidy_day', 'relative_humidy_night', 'wind_from_day', 'wind_from_night', 'wind_speed_day', 'wind_speed_night', 'wind_gust_day', 'wind_gust_night', 'sunset', 'sunrise', 'created')
#     list_per_page = 20

# Register your models here.
admin.site.register(Map)
admin.site.register(TemperatureAndRelativeHumidity)
admin.site.register(SummaryForecast)
