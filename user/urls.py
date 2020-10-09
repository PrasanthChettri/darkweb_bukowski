from django.contrib import admin
from django.urls import path  , include
from . import views

app_name = 'user'
urlpatterns = [
    path('account/', views.account , name = 'account'),
    path('login/', views.login , name = 'login'),
    path('logout/', views.logout , name = 'logout'),
    path('profile/', views.profile , name = 'profile'),
    path('signin/', views.signin , name = 'signin'),
    path('signauth/', views.signauth , name = 'signauth'),
]
