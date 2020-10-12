from django.contrib import admin
from django.urls import path  , include
from . import views

app_name = "home" 
urlpatterns = [
    path('', views.frontpage , name = 'feed'),
    path('<int:pk>', views.frontpage , name = 'feed'),
    path('topliterature', views.TopLiteratureView , name = 'topliterature'),
    path('new', views.getStarred , name = 'starred'),
    path('updatelike' , views.updatevalidate , name = "updatevalidate")
]