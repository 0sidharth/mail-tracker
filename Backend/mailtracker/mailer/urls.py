from django.urls import path
from . import views

app_name='mailer'
urlpatterns = [
	path('login/', views.login_for_gmail, name='loginforgmail'),
	path('', views.profile, name='profile'),
	path('database/', views.database, name='database'),
	path('addprof/', views.firstmail, name='firstmail'),
	path('update_seen_reply_status/', views.update_seen_reply_status, name='update_seen_reply_status'),
	path('update_send_mail/', views.update_send_mail, name='update_send_mail'),
]