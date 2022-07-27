from django.urls import path
from pages import views

urlpatterns = [
    path('', views.pages, name='index'),
    # path('todays-forecast/', views.pages, name='todays-forecast'),
    path('about/', views.about, name='about'),
    path('moderator/<str:pk>/', views.moderator, name='moderator'),
]
