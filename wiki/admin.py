from django.contrib import admin
from .models import BattleCat

@admin.register(BattleCat)
class BattleCatAdmin(admin.ModelAdmin):
    # Які колонки ми будемо бачити в списку котів
    list_display = ('title', 'status', 'hp_stat', 'dps_stat', 'author', 'created_at')
    
    # Фільтр праворуч (можна відсіяти тільки котів потрібної рідкості)
    list_filter = ('status', 'is_published')
    
    # Пошуковий рядок (шукає кота за ім'ям або описом)
    search_fields = ('title', 'content')
