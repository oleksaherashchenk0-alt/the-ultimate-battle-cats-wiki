from django.shortcuts import render, get_object_or_404
from .models import BattleCat

# Головна сторінка з помаранчевою кнопкою UNITS
def home(request):
    cats = BattleCat.objects.all()
    return render(request, 'wiki/index.html', {'cats': cats})

# Сторінка головного лобі-меню рідкісностей (Без списку котів)
def units_menu(request):
    return render(request, 'wiki/units_menu.html')

# НОВА СТОРІНКА: Окремий екран зі списком котів вибраної рідкісності
def cats_list(request):
    rarity_filter = request.GET.get('rarity', 'normal')
    cats = BattleCat.objects.filter(status=rarity_filter, is_published=True)
    return render(request, 'wiki/cats_list.html', {
        'cats': cats,
        'current_rarity': rarity_filter
    })

# Особиста сторінка окремого кота (Світліший тон)
def cat_detail(request, cat_id):
    cat = get_object_or_404(BattleCat, id=cat_id)
    return render(request, 'wiki/cat_detail.html', {'cat': cat})
