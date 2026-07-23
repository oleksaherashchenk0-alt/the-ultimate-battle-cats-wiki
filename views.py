from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import BattleCat, Ability

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

    # Здібності без опису (Single Attack, Area Attack і т.д.) не мають
    # займати свій окремий рядок - вони "приклеюються" іконкою до
    # рядка НАСТУПНОЇ здібності (з описом чи без - без різниці).
    # Якщо здібність без опису опиняється останньою в списку (нема до
    # чого приліпитись) - показуємо її саму, своїм рядком.
    ability_rows = []
    pending_icons = []
    for ability in cat.abilities.all():
        if ability.icon_only:
            pending_icons.append(ability)
        else:
            ability_rows.append({'prefix_icons': pending_icons, 'ability': ability})
            pending_icons = []
    if pending_icons:
        ability_rows.append({'prefix_icons': pending_icons, 'ability': None})

    return render(request, 'wiki/cat_detail.html', {
        'cat': cat,
        'cat_forms_json': forms_data,
        'ability_rows': ability_rows,
    })


# Старе посилання /cat/4/ (за ID) - 301-редирект на нове красиве
# /cat/dark-cat/ (за slug), щоб старі закладки й посилання не ламались
def cat_detail_legacy_redirect(request, cat_id):
    cat = get_object_or_404(BattleCat, id=cat_id)
    return redirect(reverse('cat_detail', args=[cat.slug]), permanent=True)


# Довідникова сторінка з ПОВНИМ описом усіх здібностей - кнопка
# "Show more" на сторінці кота веде сюди (на конкретну здібність,
# через якір #ability-<id>), замість того щоб розгортати текст на
# місці. Показуємо тільки здібності, у яких взагалі є що читати
# (icon_only тут не потрібні - там і так усе видно з іконки).
def abilities_list(request):
    abilities = Ability.objects.filter(icon_only=False).order_by('name')
    return render(request, 'wiki/abilities_list.html', {'abilities': abilities})
