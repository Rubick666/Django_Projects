from django.urls import path 
from . import views

urlpatterns = [ 
	path('counter',views.counter, name='counter'),
    path('', views.home, name="home")
]
