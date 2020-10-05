from django.contrib import admin
from django.urls import path  , include
from . import views

app_name = "home" 
urlpatterns = [
    path('', views.frontpage , name = 'feed'),
    path('popular', views.getpopular , name = 'popular'),
    path('new', views.getnew , name = 'new'),
]
