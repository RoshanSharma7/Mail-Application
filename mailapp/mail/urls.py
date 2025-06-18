from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('smtp-settings/', views.smtp_settings_view, name='smtp_settings'),
    path('send-mail/', views.send_mail_view, name='send_mail'),
    path('delete_mail/<int:mail_id>/', views.delete_mail, name='delete_mail'),
]
