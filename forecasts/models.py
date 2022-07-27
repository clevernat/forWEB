from django.db import models
from datetime import datetime
import uuid
# from forecasts.models import Map, TemperatureAndRelativeHumidity, SummaryForecast

# Create your models here.


class Map(models.Model):
    summary = models.OneToOneField(
        'SummaryForecast', on_delete=models.CASCADE, null=True, blank=True)
    temp_rh = models.OneToOneField(
        'TemperatureAndRelativeHumidity', on_delete=models.CASCADE, null=True, blank=True)
    utc_date = models.CharField(max_length=200, blank=True)
    featured_map = models.ImageField(
        null=True, upload_to='images/maps/')
    created = models.DateTimeField(default=datetime.now, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.created.date())


class TemperatureAndRelativeHumidity(models.Model):
    # maps = models.OneToOneField(
    #     Map, on_delete=models.CASCADE, null=True, blank=True)
    summary = models.OneToOneField(
        'SummaryForecast', on_delete=models.CASCADE, null=True, blank=True)
    utc_date = models.CharField(max_length=200, blank=True,)
    featured_graph = models.ImageField(
        null=True, upload_to='images/graphs/')
    created = models.DateTimeField(default=datetime.now, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.created.date())


class SummaryForecast(models.Model):
    # maps = models.OneToOneField(
    #     Map, on_delete=models.CASCADE, null=True, blank=True)
    # temp_rh = models.OneToOneField(
    #     'TemperatureAndRelativeHumidity', on_delete=models.CASCADE, null=True, blank=True)
    utc_date = models.CharField(max_length=200)
    temperature_day = models.IntegerField()
    temperature_night = models.IntegerField()
    rain_day = models.CharField(max_length=255)
    rain_night = models.CharField(max_length=255)
    probability_day = models.IntegerField()
    probability_night = models.IntegerField()
    relative_humidy_day = models.IntegerField()
    relative_humidy_night = models.IntegerField()
    wind_from_day = models.CharField(max_length=255)
    wind_from_night = models.CharField(max_length=255)
    wind_speed_day = models.IntegerField()
    wind_speed_night = models.IntegerField()
    wind_gust_day = models.IntegerField()
    wind_gust_night = models.IntegerField()
    sunset = models.DateTimeField(default=datetime.now, blank=True)
    sunrise = models.DateTimeField(default=datetime.now, blank=True)
    created = models.DateTimeField(default=datetime.now, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.created.date())
