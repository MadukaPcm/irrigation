from django.urls import path
from .import views
from django.contrib import admin

urlpatterns = [
    path('',views.members),
    path('uploadsensors/',views.uploadsensors),
    path('uploadsetting/',views.uploadsetting),
    path('reading/',views.members),
    path('set/',views.set), 
    path('set/uploadsettingWeb/',views.uploadsettingWeb),
    path('get_readings/',views.getReading),
    path('upload_data/', views.upload_data, name='upload_data'),

    
]