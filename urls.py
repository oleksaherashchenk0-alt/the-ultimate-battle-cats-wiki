from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('units/', views.units_menu, name='units_menu'), # Наше основне інтерактивне меню
    path('abilities/', views.abilities_list, name='abilities_list'),
    # Старе посилання виду /cat/4/ (число) - лишаємо ТОЧНО на тій самій
    # адресі, як і було раніше, тільки тепер це 301-редирект на нову
    # красиву адресу /cat/dark-cat/. Має стояти ПЕРЕД slug-шаблоном
    # нижче, інакше Django сприйме "2" за slug (це теж валідний slug)
    # і ніколи не дійде до цього рядка.
    path('cat/<int:cat_id>/', views.cat_detail_legacy_redirect, name='cat_detail_legacy'),
    path('cat/<slug:cat_slug>/', views.cat_detail, name='cat_detail'),
]
