# Generated manually: adds DE/ES/JA translation fields for cat title and content

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0005_remove_frame_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='battlecat',
            name='title_de',
            field=models.CharField(blank=True, max_length=150, verbose_name="Ім'я (DE)"),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='title_es',
            field=models.CharField(blank=True, max_length=150, verbose_name="Ім'я (ES)"),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='title_ja',
            field=models.CharField(blank=True, max_length=150, verbose_name="Ім'я (JA)"),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='content_de',
            field=models.TextField(blank=True, verbose_name='Опис (DE)'),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='content_es',
            field=models.TextField(blank=True, verbose_name='Опис (ES)'),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='content_ja',
            field=models.TextField(blank=True, verbose_name='Опис (JA)'),
        ),
    ]
