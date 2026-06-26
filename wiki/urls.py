from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                     # Головна сторінка вікі
    path('cat/<int:cat_id>/', views.cat_detail, name='cat_detail'), # Сторінка окремого кота (Урок 7)
]
