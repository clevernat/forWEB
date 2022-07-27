from django.urls import path
from forecasts import views


urlpatterns = [

    # all forecast
    path('', views.forecasts, name='forecasts'),


    path('maps/', views.maps, name='maps'),
    path('map/<str:pk>/', views.map, name='map'),


    path('temperature-relative-humidity-graphs/',
         views.temperatures_relative_humidity_graphs, name='temperature-rh-graphs'),
    path('temperature-relative-humidity-graph/<str:pk>/',
         views.temperatures_relative_humidity_graph, name='temperature-rh-graph'),



    path('summary-forecasts/', views.summary_forecasts, name='summary-forecasts'),

    path('summary-forecast/<str:pk>/',
         views.summary_forecast, name='summary-forecast'),
]
