
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('exercise/', views.exercise, name='exercise'),
    path('about/', views.about, name='about'),
    path('abs/', views.abs, name='abs'),
    path('chest/', views.chest, name='chest'),
    path('search/', views.search, name='search'),
    ]
