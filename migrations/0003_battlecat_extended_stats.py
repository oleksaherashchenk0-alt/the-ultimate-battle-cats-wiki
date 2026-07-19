# Generated manually to add extended battle-stat fields to BattleCat

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_alter_battlecat_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='battlecat',
            name='attack_power',
            field=models.IntegerField(default=0, verbose_name='Урон (Attack Power)'),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='knockback_count',
            field=models.IntegerField(default=1, verbose_name='Количество отталкиваний (Knockbacks)'),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='attack_range',
            field=models.IntegerField(default=0, verbose_name='Дальность атаки (Range)'),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='move_speed',
            field=models.IntegerField(default=0, verbose_name='Скорость перемещения (Speed)'),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='attack_frequency_seconds',
            field=models.FloatField(default=0.0, verbose_name='Частота атак, сек (Attack Frequency)'),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='attack_frequency_frames',
            field=models.IntegerField(default=0, verbose_name='Частота атак, кадри'),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='foreswing_seconds',
            field=models.FloatField(default=0.0, verbose_name='Анімація перед ударом, сек (Foreswing)'),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='foreswing_frames',
            field=models.IntegerField(default=0, verbose_name='Анімація перед ударом, кадри'),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='recharge_min_seconds',
            field=models.FloatField(default=0.0, verbose_name='Мін. час перезарядки, сек (Recharge)'),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='recharge_max_seconds',
            field=models.FloatField(default=0.0, verbose_name='Макс. час перезарядки, сек (Recharge)'),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='cost_chapter1',
            field=models.IntegerField(default=0, verbose_name='Стоимость призыва, Гл. 1 (¢)'),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='cost_chapter2',
            field=models.IntegerField(default=0, verbose_name='Стоимость призыва, Гл. 2 (¢)'),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='cost_chapter3',
            field=models.IntegerField(default=0, verbose_name='Стоимость призыва, Гл. 3 (¢)'),
        ),
    ]
