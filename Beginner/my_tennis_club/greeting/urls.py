from django.urls import path
from django.conf import settings
from django.contrib import admin
from . import views

urlpatterns = [
    path('greeting/', views.members, name='greeting'),
    path('greeting/details/<int:id>', views.datails, name='details'),
    path('', views.main, name='main'),
    path('testing/', views.testing, name="testing"),
    path('login/', views.login_page, name="login_page"),
    path('register/', views.register_page, name="register_page"),
]