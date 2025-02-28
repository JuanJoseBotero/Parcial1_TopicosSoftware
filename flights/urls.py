from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('registerPost/', views.registerPost, name='registerPost'),
    path('list/', views.listFlights, name='list'),
    path('statistics/', views.statistics, name='statistics'),
]