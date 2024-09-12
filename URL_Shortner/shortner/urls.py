from django.contrib import admin
from django.urls import path,include
from shortner import views

urlpatterns = [
    path("",views.HomePage,name='home'),
    path('<str:short_url>/', views.redirect_to_long_url, name='redirect'),
]