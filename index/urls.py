from django.contrib import admin
from django.urls import path  , include
from . import views

app_name = "home" 
urlpatterns = [
    path('', views.frontpage , name = 'feed'),
    path('popular', views.getNew , name = 'new'),
    path('new', views.getStarred , name = 'starred'),
]