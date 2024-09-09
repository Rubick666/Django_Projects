# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from Payment import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Payment.urls'))
]
