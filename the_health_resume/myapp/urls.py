from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup', views.signup, name='Signup'),
    path('dashboard', views.dashboard, name='Dashboard')
]
