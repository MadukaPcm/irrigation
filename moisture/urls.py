from django.urls import path
from .import views
from django.contrib import admin

urlpatterns = [
    path('',views.members),
    path('uploadsensors/',views.uploadsensors),
    path('uploadsetting/',views.uploadsetting),
    path('reading/',views.members),
    path('set/',views.set),
    path('uploadsettingWeb/',views.uploadsettingWeb),
]