from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Пустая строка '' означает корень сайта
    path('', views.dashboard, name='dashboard'),
    path('configure_ip/', views.configure_ip, name='configure_ip'),
    path('ping/', views.diagnostic_ping, name='ping'),
    path('sniff/', views.sniff_traffic, name='sniff'),
]