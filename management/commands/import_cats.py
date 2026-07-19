# -*- coding: utf-8 -*-
"""
Команда масового імпорту котів з CSV-файлу.

Навіщо: заповнювати 2000+ котів по одному в адмінці - нереально.
Натомість заповнюєш звичайну таблицю (Google Sheets / Excel), експортуєш
у CSV і одним запуском команди заливаєш усе (або оновлюєш вже наявних
котів, якщо запустиш команду ще раз з оновленим файлом).

Використання:
    python manage.py import_cats шлях/до/файлу.csv
    python manage.py import_cats шлях/до/файлу.csv --author=admin

Якщо --author не вказано - береться перший суперюзер у базі.

Формат CSV дивись у cats_import_template.csv (додається окремо).
Колонка "title" - обов'язкова і використовується як унікальний ключ:
якщо кіт з такою назвою вже є в базі - він ОНОВЛЮЄТЬСЯ, а не дублюється.
Це дозволяє спокійно допрацьовувати таблицю і перезаливати скільки завгодно разів.
"""

import csv

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from wiki.models import BattleCat


# Колонки CSV -> поля моделі. Ключ = заголовок стовпця в CSV (як є, без змін),
# значення = (назва поля в моделі, функція перетворення рядка у потрібний тип)
def _int(v, default=0):
    v = (v or '').strip()
    return int(float(v)) if v else default


def _float(v, default=0.0):
    v = (v or '').strip()
    return float(v) if v else default


def _bool(v, default=True):
    v = (v or '').strip().lower()
    if v in ('0', 'false', 'no', 'ні', 'нет'):
        return False
    if v in ('1', 'true', 'yes', 'так', 'да'):
        return True
    return default


FIELD_MAP = {
    'content': ('content', str),
    'title_de': ('title_de', str),
    'title_es': ('title_es', str),
    'title_ja': ('title_ja', str),
    'content_de': ('content_de', str),
    'content_es': ('content_es', str),
    'content_ja': ('content_ja', str),
    'mini_info': ('mini_info', str),
    'status': ('status', str),
    'hp_stat': ('hp_stat', _int),
    'attack_power': ('attack_power', _int),
    'dps_stat': ('dps_stat', _float),
    'knockback_count': ('knockback_count', lambda v: _int(v, 1)),
    'attack_range': ('attack_range', _int),
    'move_speed': ('move_speed', _int),
    'attack_frequency_seconds': ('attack_frequency_seconds', _float),
    'foreswing_seconds': ('foreswing_seconds', _float),
    'recharge_min_seconds': ('recharge_min_seconds', _float),
    'recharge_max_seconds': ('recharge_max_seconds', _float),
    'cost_chapter1': ('cost_chapter1', _int),
    'cost_chapter2': ('cost_chapter2', _int),
    'cost_chapter3': ('cost_chapter3', _int),
    'is_published': ('is_published', _bool),
}

VALID_STATUSES = {c[0] for c in BattleCat.RARITY_CHOICES}


class Command(BaseCommand):
    help = "Масово імпортує/оновлює котів з CSV-файлу (title = унікальний ключ)."

    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=str, help="Шлях до CSV-файлу з котами")
        parser.add_argument(
            '--author', type=str, default=None,
            help="Username автора, якому припишуться коти (за замовчуванням - перший суперюзер)"
        )

    def handle(self, *args, **options):
        csv_path = options['csv_path']

        # --- Визначаємо автора ---
        if options['author']:
            try:
                author = User.objects.get(username=options['author'])
            except User.DoesNotExist:
                raise CommandError(f"Користувача '{options['author']}' не знайдено.")
        else:
            author = User.objects.filter(is_superuser=True).order_by('id').first()
            if not author:
                raise CommandError(
                    "Не знайдено жодного суперюзера. Створи його: python manage.py createsuperuser "
                    "або вкажи --author=ім'я_користувача"
                )

        # --- Читаємо CSV ---
        try:
            f = open(csv_path, newline='', encoding='utf-8-sig')
        except FileNotFoundError:
            raise CommandError(f"Файл не знайдено: {csv_path}")

        with f:
            # Excel на не-англійських Windows часто зберігає CSV з роздільником ";"
            # замість "," (навіть якщо у назві формату написано "коми") - через
            # регіональні налаштування. Визначаємо роздільник автоматично за
            # першим рядком (заголовками), щоб команда працювала в обох випадках.
            first_line = f.readline()
            f.seek(0)
            delimiter = ';' if first_line.count(';') > first_line.count(',') else ','

            reader = csv.DictReader(f, delimiter=delimiter)
            if not reader.fieldnames or 'title' not in reader.fieldnames:
                raise CommandError(
                    "У CSV обов'язково має бути колонка 'title'. "
                    f"Знайдені колонки: {reader.fieldnames}. "
                    "Схоже, файл зберігся з іншим роздільником стовпців, ніж очікувалось "
                    f"(автоматично визначено роздільник '{delimiter}') - "
                    "перевір, що при збереженні в Excel обрано саме 'CSV UTF-8 (роздільник кома)'."
                )

            created_count = 0
            updated_count = 0
            skipped_rows = []

            with transaction.atomic():
                for i, row in enumerate(reader, start=2):  # start=2, бо рядок 1 - заголовки
                    title = (row.get('title') or '').strip()
                    if not title:
                        skipped_rows.append((i, "порожній title"))
                        continue

                    status_raw = (row.get('status') or '').strip()
                    if status_raw and status_raw not in VALID_STATUSES:
                        skipped_rows.append((i, f"невідомий status '{status_raw}' у кота '{title}'"))
                        continue

                    defaults = {'author': author}
                    if status_raw:
                        defaults['status'] = status_raw
                    for csv_col, (field_name, caster) in FIELD_MAP.items():
                        if csv_col == 'status':
                            continue
                        if csv_col not in row:
                            continue
                        raw_val = row.get(csv_col)
                        # Порожня клітинка в CSV - НЕ чіпаємо це поле взагалі.
                        # Інакше при частковому оновленні файлу всі порожні
                        # клітинки затирали б вже наявні значення в базі
                        # нулями/пусткою (саме через це зникав mini_info).
                        if raw_val is None or raw_val.strip() == '':
                            continue
                        try:
                            defaults[field_name] = caster(raw_val)
                        except (ValueError, TypeError):
                            skipped_rows.append((i, f"погане значення в колонці '{csv_col}' у кота '{title}'"))

                    # content обов'язкове поле в моделі (без blank=True) - підстрахуємось
                    defaults.setdefault('content', '')

                    obj, was_created = BattleCat.objects.update_or_create(
                        title=title, defaults=defaults
                    )

                    if was_created:
                        created_count += 1
                    else:
                        updated_count += 1

        self.stdout.write(self.style.SUCCESS(
            f"Готово! Створено: {created_count}, оновлено: {updated_count}."
        ))
        if skipped_rows:
            self.stdout.write(self.style.WARNING(f"Пропущено рядків: {len(skipped_rows)}"))
            for row_num, reason in skipped_rows[:30]:
                self.stdout.write(f"  рядок {row_num}: {reason}")
            if len(skipped_rows) > 30:
                self.stdout.write(f"  ...і ще {len(skipped_rows) - 30}")
