# Generated manually: adds mini_info tooltip field and fixes is_published default

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0003_battlecat_extended_stats'),
    ]

    operations = [
        migrations.AddField(
            model_name='battlecat',
            name='mini_info',
            field=models.CharField(
                blank=True, max_length=200,
                verbose_name='Коротка інфо при наведенні (спливаюча підказка)'
            ),
        ),
        migrations.AlterField(
            model_name='battlecat',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
