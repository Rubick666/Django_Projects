from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
	path('logout/', views.logout, name="logout"),
	path('pdf/', views.pdf , name='pdf'),
	path('admin/', admin.site.urls),
	path('login/' , views.login_page, name='login'),
	path('register/', views.register_page, name='register'),
	
	path('', views.recipes, name='recipes'),
	path('update/<id>', views.update, name='update'),
	path('delete/<id>', views.delete, name='delete'),
]
