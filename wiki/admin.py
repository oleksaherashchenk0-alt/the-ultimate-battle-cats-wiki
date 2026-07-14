from django.contrib import admin
from .models import BattleCat, Ability


@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
    # Окремий розділ в адмінці "Здібності" - тут ведеш каталог
    # (назва + іконка + опис), а потім прив'язуєш потрібні коту
    # галочками в самій картці кота нижче
    list_display = ('name', 'icon')
    search_fields = ('name',)


@admin.register(BattleCat)
class BattleCatAdmin(admin.ModelAdmin):
    # Які колонки ми будемо бачити в списку котів
    list_display = ('title', 'status', 'hp_stat', 'dps_stat', 'attack_power', 'author', 'created_at')
    
    # Фільтр праворуч (можна відсіяти тільки котів потрібної рідкості)
    list_filter = ('status', 'is_published')
    
    # Пошуковий рядок (шукає кота за ім'ям або описом)
    search_fields = ('title', 'content')

    # Зручний віджет для вибору здібностей - дві колонки з пошуком
    # (доступні зліва -> обрані справа), а не довгий список чекбоксів
    filter_horizontal = ('abilities',)

    # Групуємо поля редагування картки кота на зручні блоки:
    # основне, бойові статы, швидкість атаки/перезарядка, вартість призиву
    fieldsets = (
        ('Основне', {
            'fields': ('title', 'content', 'mini_info', 'image', 'status', 'is_published', 'author')
        }),
        ('Переклади імені й опису (необов\'язково - якщо не заповнити, покаже англійську)', {
            'fields': ('title_de', 'content_de', 'title_es', 'content_es', 'title_ja', 'content_ja'),
            'classes': ('collapse',),  # згорнутий блок, щоб не заважав, поки не треба
        }),
        ('Бойові характеристики', {
            'fields': ('hp_stat', 'attack_power', 'dps_stat', 'knockback_count', 'attack_range', 'move_speed')
        }),
        ('Швидкість атаки та перезарядка', {
            'fields': (
                'attack_frequency_seconds',
                'foreswing_seconds',
                'recharge_min_seconds', 'recharge_max_seconds',
            )
        }),
        ('Економіка в бою', {
            'fields': ('cost_chapter1', 'cost_chapter2', 'cost_chapter3')
        }),
        ('Трейти (по яких типах ворогів кіт ефективний)', {
            'fields': (
                'hits_red', 'hits_floating', 'hits_black', 'hits_metal', 'hits_angel',
                'hits_alien', 'hits_zombie', 'hits_relic', 'hits_aku',
            )
        }),
        ('Здібності', {
            'fields': ('abilities',)
        }),
    )
