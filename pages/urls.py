from django.urls import path
from pages import views

urlpatterns = [
    path('', views.pages, name='index'),
    path('moderator/<str:pk>/', views.moderator, name='moderator'),
]
