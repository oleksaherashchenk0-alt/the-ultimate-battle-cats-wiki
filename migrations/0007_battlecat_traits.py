# Generated manually: adds trait boolean fields (Red, Floating, Black, Metal,
# Angel, Alien, Zombie, Relic, Aku) - shown as grayscale/colored icons on cat page

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0006_cat_title_content_translations'),
    ]

    operations = [
        migrations.AddField(
            model_name='battlecat',
            name='hits_red',
            field=models.BooleanField(default=False, verbose_name='Red'),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='hits_floating',
            field=models.BooleanField(default=False, verbose_name='Floating'),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='hits_black',
            field=models.BooleanField(default=False, verbose_name='Black'),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='hits_metal',
            field=models.BooleanField(default=False, verbose_name='Metal'),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='hits_angel',
            field=models.BooleanField(default=False, verbose_name='Angel'),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='hits_alien',
            field=models.BooleanField(default=False, verbose_name='Alien'),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='hits_zombie',
            field=models.BooleanField(default=False, verbose_name='Zombie'),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='hits_relic',
            field=models.BooleanField(default=False, verbose_name='Relic'),
        ),
        migrations.AddField(
            model_name='battlecat',
            name='hits_aku',
            field=models.BooleanField(default=False, verbose_name='Aku'),
        ),
    ]
