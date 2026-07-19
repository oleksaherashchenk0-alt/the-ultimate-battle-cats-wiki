from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import BattleCat

# Головна сторінка з помаранчевою кнопкою UNITS
# Коти більше не виводяться тут списком - вони показуються на сторінці
# /units/, кожен у своїй колонці-акордеоні за рідкістю.
def home(request):
    return render(request, 'wiki/index.html')

# Головне меню з горизонтальним рядом та висувною плашкою
def units_menu(request):
    # Отримуємо списки котів окремо для кожної ігрової рідкісності
    cats_by_rarity = {
        'normal': BattleCat.objects.filter(status='normal', is_published=True),
        'special': BattleCat.objects.filter(status='special', is_published=True),
        'rare': BattleCat.objects.filter(status='rare', is_published=True),
        'super_rare': BattleCat.objects.filter(status='super_rare', is_published=True),
        'uber_rare': BattleCat.objects.filter(status='uber_rare', is_published=True),
        'legend_rare': BattleCat.objects.filter(status='legend_rare', is_published=True),
        'limited': BattleCat.objects.filter(status='limited', is_published=True),
    }
    
    return render(request, 'wiki/units_menu.html', {
        'cats_by_rarity': cats_by_rarity
    })

# Особиста сторінка окремого кота (Світліший тон)
def cat_detail(request, cat_slug):
    cat = get_object_or_404(BattleCat, slug=cat_slug)

    # Форма 0 - завжди сам кіт (Base Form), далі йдуть CatForm-записи
    # (Evolved/True/Ultra), у тому порядку, який заданий полем "order"
    forms_data = [{
        'name': cat.title,
        'name_de': cat.title_de,
        'name_es': cat.title_es,
        'name_ja': cat.title_ja,
        'icon': cat.image.url if cat.image else '',
        'hp_stat': cat.hp_stat,
        'attack_power': cat.attack_power,
        'dps_stat': cat.dps_stat,
    }]
    for form in cat.forms.all():
        forms_data.append({
            'name': form.name,
            'name_de': form.name_de,
            'name_es': form.name_es,
            'name_ja': form.name_ja,
            'icon': form.icon.url if form.icon else '',
            'hp_stat': form.hp_stat,
            'attack_power': form.attack_power,
            'dps_stat': form.dps_stat,
        })

    return render(request, 'wiki/cat_detail.html', {
        'cat': cat,
        'cat_forms_json': forms_data,
    })


# Старе посилання /cat/4/ (за ID) - 301-редирект на нове красиве
# /cat/dark-cat/ (за slug), щоб старі закладки й посилання не ламались
def cat_detail_legacy_redirect(request, cat_id):
    cat = get_object_or_404(BattleCat, id=cat_id)
    return redirect(reverse('cat_detail', args=[cat.slug]), permanent=True)
