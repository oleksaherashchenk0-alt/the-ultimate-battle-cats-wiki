from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('units/', views.units_menu, name='units_menu'), # Наше основне інтерактивне меню
    path('cat/<int:cat_id>/', views.cat_detail, name='cat_detail'),
]
