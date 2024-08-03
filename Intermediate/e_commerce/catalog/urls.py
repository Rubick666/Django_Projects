from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name="product_list"),
    path('home/', views.home, name="home"),
    path('<int:pk>/', views.product_detail, name="product_detail"),
    path('cart/', views.view_cart, name="view_cart"),
    path('add/<int:id>', views.add_to_cart, name="add_to_cart"),
    path('remove/<int:id>', views.remove_from_cart, name="remove_from_cart")
]