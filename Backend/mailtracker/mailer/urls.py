from django.urls import path
from . import views

app_name='mailer'
urlpatterns = [
	path('login/', views.login_for_gmail, name='loginforgmail'),
	path('', views.profile, name='profile'),
	path('database/', views.database, name='database'),
]