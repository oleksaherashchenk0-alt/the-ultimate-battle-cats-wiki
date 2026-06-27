from django.db import models
from django.contrib.auth.models import User

class BattleCat(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to='cats/', blank=True, null=True)
    hp_stat = models.IntegerField(default=0)
    dps_stat = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
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
