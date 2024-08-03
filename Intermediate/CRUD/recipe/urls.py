from django.urls import path
from .views import *
from django.contrib import admin

urlpatterns = [
    path('', recipes),
    path('upadte_recipe/<int:id>/', update_recipe, name="update_recipe"),
    path('delete_recipe/<int:id>', delete_recipe, name="delete_recipe")
]