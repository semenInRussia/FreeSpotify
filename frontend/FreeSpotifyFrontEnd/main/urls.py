from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('top/', views.view_top, name='top')
]
