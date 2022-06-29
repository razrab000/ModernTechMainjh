from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Main),
    path('background', views.Background),
    path('contact', views.Contact)
]
