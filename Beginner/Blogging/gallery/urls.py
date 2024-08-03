from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.product_list, name="product_list"),
    path('<int:pk>/', views.product_detail, name="product_detail"),
    path('<int:pk>/edit/', views.edit_product, name="edit_product"),
    path('<int:pk>/delete/', views.delete_product, name="delete_product"),
    ]