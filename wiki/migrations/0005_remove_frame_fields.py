# Generated manually: removes attack_frequency_frames and foreswing_frames -
# user decided frame counts weren't needed, only seconds are shown

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0004_battlecat_mini_info_and_published_default'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='battlecat',
            name='attack_frequency_frames',
        ),
        migrations.RemoveField(
            model_name='battlecat',
            name='foreswing_frames',
        ),
    ]
