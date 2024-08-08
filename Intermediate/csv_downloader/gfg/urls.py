from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('generate_csv/', views.generate_csv, name="generate_csv"),
    
]