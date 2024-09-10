# myproject/urls.py

from django.contrib import admin
from django.urls import path
from Payment import views
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ensure_csrf_cookie(views.index), name='index'),
    path('create-checkout-session/', views.create_checkout_session, name='create-checkout-session'),
    path('webhook/', csrf_exempt(views.handle_webhook), name='webhook'),
]