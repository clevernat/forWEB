from django.shortcuts import redirect, render
from forecasts.models import Map, TemperatureAndRelativeHumidity, SummaryForecast

# Create your views here.


def forecasts(request):
    return render(request, 'forecasts/forecasts.html')


def maps(request):
    maps = Map.objects.order_by('-created').all()

    context = {'maps': maps}
    return render(request, 'forecasts/maps.html', context)


def map(request, pk):
    # map
    map = Map.objects.order_by('-created').get(id=pk)

    context = {'map': map}
    return render(request, 'forecasts/map.html', context)


def temperatures_relative_humidity_graphs(request):
    temperature_humidity_graphs = TemperatureAndRelativeHumidity.objects.order_by(
        '-created').all()

    context = {'temperature_humidity_graphs': temperature_humidity_graphs}
    return render(request, 'forecasts/temp-rh-profiles.html', context)


def temperatures_relative_humidity_graph(request, pk):
    temperatures_relative_humidity_graph = TemperatureAndRelativeHumidity.objects.order_by(
        'created').get(id=pk)

    context = {
        'temperatures_rh_graph': temperatures_relative_humidity_graph}
    return render(request, 'forecasts/temp-rh-profile.html', context)


def summary_forecasts(request):
    summary_forecasts = SummaryForecast.objects.order_by('-created').all()
    context = {'summary_forecasts': summary_forecasts}
    return render(request, 'forecasts/summary-forecasts.html', context)


def summary_forecast(request, pk):
    summary_forecast = SummaryForecast.objects.order_by('-created').get(id=pk)

    context = {'summary_forecast': summary_forecast}
    return render(request, 'forecasts/summary-forecast.html', context)


# a = [1, 2, 3, 4, 5]
# print(a[0])
