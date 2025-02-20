from django.contrib import admin
from django.urls import path
from hello import views

urlpatterns = [
    path('', views.index, name='home'),
    path('сhange_the_boundaries', views.image),
    path('cipher', views.cipher),
    path('pilots', views.audio),
    path('final', views.final)
]
