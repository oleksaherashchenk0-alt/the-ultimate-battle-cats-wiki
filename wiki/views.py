from django.shortcuts import render, get_object_or_404
from .models import BattleCat

# Головна сторінка
def home(request):
    cats = BattleCat.objects.all()
    return render(request, 'wiki/index.html', {'cats': cats})

# Окрема сторінка кота
def cat_detail(request, cat_id):
    cat = get_object_or_404(BattleCat, id=cat_id)
    return render(request, 'wiki/cat_detail.html', {'cat': cat})
