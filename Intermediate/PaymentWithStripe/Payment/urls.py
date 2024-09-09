# myproject/urls.py

from django.contrib import admin
from django.urls import path
from Payment import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('create-checkout-session/', views.create_checkout_session, name='create-checkout-session'),
    path('webhook/', views.handle_webhook, name='webhook'),
]
