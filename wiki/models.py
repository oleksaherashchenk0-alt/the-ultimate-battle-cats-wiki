from django.db import models
from django.contrib.auth.models import User


class Ability(models.Model):
    """
    Каталог здібностей (Strong Against, Knockback, Freeze, Weaken і т.д.).
    Кожна здібність існує один раз тут, а котам просто прив'язуєш потрібні
    галочками в адмінці - додати нову здібність більше НЕ вимагає нової
    міграції бази, просто додаєш нову картку тут.
    """
    name = models.CharField("Назва здібності", max_length=100, unique=True)
    icon = models.ImageField("Іконка", upload_to='abilities/', blank=True, null=True)
    description = models.TextField(
        "Опис (наприклад: 'Deals 1.5x damage, only takes 1/2 damage')",
        blank=True
    )

    # Переклади назви й опису здібності на інші мови сайту (EN = поля
    # name/description вище, вони лишаються базовими "за замовчуванням").
    # Якщо переклад для якоїсь мови не заповнено - на сайті показується
    # англійська версія (той самий принцип, що і в BattleCat).
    name_de = models.CharField("Назва (DE)", max_length=100, blank=True)
    name_es = models.CharField("Назва (ES)", max_length=100, blank=True)
    name_ja = models.CharField("Назва (JA)", max_length=100, blank=True)
    description_de = models.TextField("Опис (DE)", blank=True)
    description_es = models.TextField("Опис (ES)", blank=True)
    description_ja = models.TextField("Опис (JA)", blank=True)

    class Meta:
        verbose_name = "Здібність"
        verbose_name_plural = "Здібності"
        ordering = ['name']

    def __str__(self):
        return self.name


class BattleCat(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to='cats/', blank=True, null=True)
    hp_stat = models.IntegerField(default=0)
    dps_stat = models.FloatField(default=0.0)

    # Переклади імені й опису кота на інші мови сайту (EN = поля title/content
    # вище, вони й лишаються базовими "за замовчуванням"). Якщо переклад для
    # якоїсь мови не заповнено - на сайті просто показується англійська версія.
    title_de = models.CharField("Ім'я (DE)", max_length=150, blank=True)
    title_es = models.CharField("Ім'я (ES)", max_length=150, blank=True)
    title_ja = models.CharField("Ім'я (JA)", max_length=150, blank=True)
    content_de = models.TextField("Опис (DE)", blank=True)
    content_es = models.TextField("Опис (ES)", blank=True)
    content_ja = models.TextField("Опис (JA)", blank=True)

    # Коротка інфо, яка з'являється у спливаючій підказці (tooltip) при наведенні
    # на фото кота в списку рідкості - на відміну від content (повний опис на сторінці кота)
    mini_info = models.CharField(
        "Коротка інфо при наведенні (спливаюча підказка)",
        max_length=200, blank=True
    )

    # --- Розширені бойові характеристики (показуються в таблиці на сторінці кота) ---
    attack_power = models.IntegerField("Урон (Attack Power)", default=0)
    knockback_count = models.IntegerField("Количество отталкиваний (Knockbacks)", default=1)
    attack_range = models.IntegerField("Дальность атаки (Range)", default=0)
    move_speed = models.IntegerField("Скорость перемещения (Speed)", default=0)

    attack_frequency_seconds = models.FloatField("Частота атак, сек (Attack Frequency)", default=0.0)
    foreswing_seconds = models.FloatField("Анімація перед ударом, сек (Foreswing)", default=0.0)

    recharge_min_seconds = models.FloatField("Мін. час перезарядки, сек (Recharge)", default=0.0)
    recharge_max_seconds = models.FloatField("Макс. час перезарядки, сек (Recharge)", default=0.0)

    cost_chapter1 = models.IntegerField("Стоимость призыва, Гл. 1 (¢)", default=0)
    cost_chapter2 = models.IntegerField("Стоимость призыва, Гл. 2 (¢)", default=0)
    cost_chapter3 = models.IntegerField("Стоимость призыва, Гл. 3 (¢)", default=0)

    # --- Трейти (типи ворогів), по яких кіт б'є ефективніше -
    # іконка сіра за замовчуванням, кольорова якщо True.
    # Список стандартний для гри: Red, Floating, Black, Metal, Angel,
    # Alien, Zombie, Relic, Aku.
    hits_red = models.BooleanField("Red", default=False)
    hits_floating = models.BooleanField("Floating", default=False)
    hits_black = models.BooleanField("Black", default=False)
    hits_metal = models.BooleanField("Metal", default=False)
    hits_angel = models.BooleanField("Angel", default=False)
    hits_alien = models.BooleanField("Alien", default=False)
    hits_zombie = models.BooleanField("Zombie", default=False)
    hits_relic = models.BooleanField("Relic", default=False)
    hits_aku = models.BooleanField("Aku", default=False)
    hits_none = models.BooleanField("None", default=False)

    # Здібності кота - обираються з каталогу Ability (галочками в адмінці),
    # а не окремими полями, бо здібностей десятки й список постійно росте
    abilities = models.ManyToManyField(Ability, blank=True, related_name='cats', verbose_name="Здібності")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # За замовчуванням True - інакше новододані коти "не з'являлись" на сайті,
    # бо views.py фільтрує is_published=True, а чекбокс в адмінці треба було
    # вручну вмикати щоразу
    is_published = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Додали всі рідкісності, які є на твоїх кнопках меню
    RARITY_CHOICES = [
        ('normal', 'Normal Cat'),
        ('special', 'Special Cat'),
        ('rare', 'Rare Cat'),
        ('super_rare', 'Super Rare Cat'),
        ('uber_rare', 'Uber Rare Cat'),
        ('legend_rare', 'Legend Rare Cat'),
        ('limited', 'Limited Cat'),
    ]
    status = models.CharField(max_length=20, choices=RARITY_CHOICES, default='normal')

    def __str__(self):
        return self.title
