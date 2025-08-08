# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.filter_view, name='filters_view'),
    path('user/', views.filters_view, name='filters_view'),
]