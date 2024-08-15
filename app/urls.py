#Django
from django.contrib import admin
from django.urls import path

#Local Django
from . import views


urlpatterns = [
    path('', views.home, name='home'),
]
