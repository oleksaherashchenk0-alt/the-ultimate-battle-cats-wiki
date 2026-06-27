from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('units/', views.units_menu, name='units_menu'), # Головне меню вибору рідкісності
    path('units/list/', views.cats_list, name='cats_list'), # ОЦЕЙ РЯДОК ДУЖЕ ВАЖЛИВИЙ, ВІН ПРИБЕРЕ ПОМИЛКУ!
    path('cat/<int:cat_id>/', views.cat_detail, name='cat_detail'),
]
