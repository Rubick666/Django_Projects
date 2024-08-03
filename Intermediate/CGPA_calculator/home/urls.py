from django.urls import path
from .views import *

urlpatterns = [
    path('', cgpa_calculator, name="cgpa_calculator"),
    path('edit/<int:id>/', edit_subject, name="edit_subject"),
    path('delete/<int:id>/', delete_subject, name="delete_subject"),
    path('result/', result, name="result"),
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
    path('logout/', custom_logout, name="logout"),
]